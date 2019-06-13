from django.shortcuts import render, redirect
from .models import *
from cart.models import CartInfo
from user_manage import userlogin
from django.db import transaction
from datetime import datetime
from decimal import Decimal


# Create your views here.


@userlogin.login
def order(request):

    context = {}
    return render(request, 'order/place_order.html',context)


# 使用事务
@transaction.atomic()
@userlogin.login
def order_handle(request):
    tran_id = transaction.savepoint()
    # 接收购物车编号
    cart_ids = request.POST.get('cart_ids')
    try:
        # 创建订单
        order = OrderInfo()
        now = datetime.now()
        uid = request.session['user_id']
        order.oid = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), uid)
        order.user_id = uid
        order.odate = now
        order.ototal = Decimal(request.POST.get('total'))
        order.save()
        # 创建订单详情
        cart_idsl = [int(item) for item in cart_ids.split(',')]
        for i in cart_ids:
            detail = OrderDetailInfo()
            detail.order = order
            # 查新购物车信息
            cart = CartInfo.objects.get(id=i)
            # 处理库存
            goods = cart.goods
            if goods.stock >= cart.count:
                # 减少库存
                goods.stock = cart.goods.stock - cart.count
                goods.save()
                # 完善订单信息
                detail.goods_id = goods.id
                detail.price = goods.gprice
                detail.count = cart.count
                detail.save()
                # 删除购物车的数据
                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print('======================%s' % e)
        transaction.savepoint_rollback(tran_id)
    return redirect('/user/order/')


@userlogin.login
def pay(request, oid):
    '''支付'''

    order = OrderInfo.objects.get(oid=oid)
    order.oIsPay = True
    order.save()
    context = {'order': order}

    return render(request, 'order/pay.html', context)

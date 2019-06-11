from django.shortcuts import render,redirect
from django.http import JsonResponse
from user_manage import userlogin
from .models import *
# Create your views here.

@userlogin.login
def cart(request):
    username = request.session['user_id']
    carts = CartInfo.objects.filter(user=username)

    context = {'title':'购物车','carts':carts}

    return render(request, 'cart/cart.html', context)

@userlogin.login
def add(request,goods_id, count):
    username = request.session['user_id']
    gid = int(goods_id)
    count = int(count)

    carts = CartInfo.objects.filter(user_id=username,goods_id=gid,)
    if len(carts) > 0:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo.objects.create(user_id=username,goods_id=goods_id)
    cart.save()

    # 如果是ajax请求
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=username).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')

@userlogin.login
def edit(request, cart_id, count):
    try:
        cart = CartInfo.objects.get(pk= int(cart_id))
        count1 = cart.count=int(count)
        cart.save()
    except Exception as e:
        data = {'ok':count1}
    return JsonResponse(data)


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
        cart = CartInfo.objects.create(user_id=username,goods_id=goods_id,count=count)
    cart.save()
    # print('购物车')
    # print(cart.user,cart.goods)
    # 如果是ajax请求,不跳转
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
        data = {'ok': 0}
    except Exception as e:
        data = {'ok':count1}
    return JsonResponse(data)

@userlogin.login
def delete(request,cart_id):
    try:
        print('delete',cart_id)
        cart = CartInfo.objects.get(id=cart_id)
        cart.delete()
        data = {'ok':1}
    except Exception as e:
        data = {'ok':0}
    return JsonResponse(data)
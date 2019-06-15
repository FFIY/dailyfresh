from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
import hashlib
from . import userlogin
from goods.models import GoodInfo

# Create your views here.


def index(request):
    context = {'title': '天天生鲜-首页', 'request':request}
    return render(request, 'user_manage/../templates/index.html', context)


def register(request):
    # 注册用户
    if request.method == 'POST':
        # 获取用户注册信息
        uname = request.POST.get('user_name')
        upassword = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')
        # 判断两次密码是否一致
        if upassword != cpwd or not uname:
            return redirect('/user/register/')
        # 加密用户密码
        pwd = hashlib.sha1(upassword.encode('utf-8'))
        # 创建用户
        user = UserInfo(uname=uname, upassword=pwd.hexdigest(), email=email)
        # 保存用户信息到数据库
        user.save()
        return redirect('/user/login/')
    else:
        # 其他请求方法
        context = {'request':request}
        return render(request, 'user_manage/register.html', context)


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('pwd')
        remember = request.POST.get('remember', 0)
        users = UserInfo.objects.filter(uname=uname)
        print(uname, pwd, remember, users)
        if users:
            s1 = hashlib.sha1(pwd.encode('utf-8'))
            if s1.hexdigest() == users[0].upassword:
                print('已经登录',request.COOKIES)
                if request.COOKIES.get('url',''):
                    # 如果已经录返回之前的页面
                    print('req url',request.COOKIES.get('url'))
                    red = HttpResponseRedirect(request.COOKIES.get('url'))
                else:
                    red = HttpResponseRedirect('/user/info/')
                if int(remember):
                    red.set_cookie('uname', uname,max_age = 60*60*24*30)
                    # red.set_cookie('user_id', uname,max_age = 60*60*24*30)
                else:
                    red.set_cookie('uname', uname, max_age=-1)
                    # red.set_cookie('user_id', uname, max_age=-1)

                request.session['user_name'] = uname
                request.session['user_id'] = uname
                return red
            else:
                context = {'title': '天天生鲜-用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'pwd': pwd}
                return render(request, 'user_manage/login.html', context)
        else:
            context = {'title': '天天生鲜-用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'pwd': pwd}
            return render(request, 'user_manage/login.html', context)
    uname = request.COOKIES.get('uname', '')
    context = {'title': '天天生鲜-用户登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname, 'request':request}
    return render(request, 'user_manage/login.html', context)


@userlogin.login
def info(request):
    uname = request.COOKIES.get('uname', '')
    # 获取最近浏览的商品id
    goods_ids = request.COOKIES.get('goodsids','')
    print(type(goods_ids),goods_ids)
    goods_list = []
    if goods_ids != '':
        for i in goods_ids.split(','):
            goods_list.append(GoodInfo.objects.get(id=int(i)))

    try:
        user = UserInfo.objects.get(uname=uname)
        user_email = user.email
    except UserInfo.DoesNotExist:
        user_email = ''

    context = {'title': '用户中心', 'user_email': user_email, 'user_name': uname,
               'goods_list':goods_list, 'request':request}
    return render(request, 'user_manage/user_center_info.html', context)


@userlogin.login
def order(request):
    # uname = request.session.get('uname','')
    # try:
    #     user = UserInfo.objects.get(uname=uname)
    #     user_email = user.uemail
    # except UserInfo.DoesNotExist:
    #     user_email = ''

    context = {'tittle': '用户中心', 'request':request}
    return render(request, 'user_manage/user_center_order.html', context)


@userlogin.login
def site(request):
    print(dir(request))
    uname = request.session.get('uname', '')
    try:
        user = UserInfo.objects.get(uname=uname)
        user_email = user.email
    except UserInfo.DoesNotExist:
        user = None
        user_email = ''
    if request.method == 'POST':
        if user:
            addressee = request.POST.get('addressee')
            uadress = request.POST.get('uadress')
            zipcode = request.POST.get('zipcode')
            phone = request.POST.get('uphone')
            print(addressee, uadress)
            print(zipcode, phone)
            if addressee and uadress and zipcode and phone:
                try:
                    UserAdress.objects.get(r_adress=uadress, r_user=addressee)
                except UserAdress.DoesNotExist as e:
                    newaddress = UserAdress(r_adress=uadress, zipcode=zipcode, r_user=addressee, r_phone=phone)
                    newaddress.save()
                else:
                    newaddress = UserAdress.objects.get(r_adress=uadress, r_user=addressee, r_phone=phone)
                user.addressee = newaddress
                user.save()
                return redirect('/user/site/')

    context = {'tittle': '用户中心', 'user': user, 'request': request}
    return render(request, 'user_manage/user_center_site.html', context)

def logout(request):

    request.session.flush()
    return redirect('/index/')

def base(request):
    context = {'tittle': 'base', 'request': request}
    return render(request, 'base.html', context)

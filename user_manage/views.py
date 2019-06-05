from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *
import hashlib

# Create your views here.


def index(request):

    context = {}
    return render(request, 'user_manage/index.html',context)


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
        user = UserInfo(uname=uname,upassword=pwd.hexdigest(),email=email)
        # 保存用户信息到数据库
        user.save()
        return redirect('/user/login/')
    else:
        # 其他请求方法
        context = {}
        return render(request, 'user_manage/register.html',context)

def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('pwd')
        remember = request.POST.get('remember',0)
        users = UserInfo.objects.filter(uname=uname)
        print(uname,pwd,remember,users)
        if users:
            s1 = hashlib.sha1(pwd.encode('utf-8'))
            if s1.hexdigest() == users[0].upassword:
                red = HttpResponseRedirect('/user/info/')
                if remember:
                    red.set_cookie('uname',uname)
                else:
                    red.set_cookie('uname','',max_age = -1)

                request.session['user_name']= uname
                return red
            else:
                context = {'title': '天天生鲜-用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname,'pwd':pwd}
                return render(request, 'user_manage/login.html', context)
        else:
            context = {'title': '天天生鲜-用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'pwd': pwd}
            return render(request, 'user_manage/login.html', context)
    uname = request.COOKIES.get('uname','')
    context = {'title':'天天生鲜-用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'user_manage/login.html',context)


def info(request):
    uname = request.session.get('uname','')
    try:
        user = UserInfo.objects.get(uname=uname)
        user_email = user.uemail
    except UserInfo.DoesNotExist:
        user_email = ''

    context = {'tittle':'用户中心', 'user_email':user_email,'user_name':uname}
    return render(request,'user_manage/user_center_info.html',context)


def order(request):
    # uname = request.session.get('uname','')
    # try:
    #     user = UserInfo.objects.get(uname=uname)
    #     user_email = user.uemail
    # except UserInfo.DoesNotExist:
    #     user_email = ''

    context = {'tittle':'用户中心'}
    return render(request,'user_manage/user_center_order.html',context)

def site(request):
    uname = request.session.get('uname','')
    try:
        user = UserInfo.objects.get(uname=uname)
        user_email = user.uemail
    except UserInfo.DoesNotExist:
        user = None
        user_email = ''
    if request.method == 'POST':
        if user:
            user.addressee = request.POST.get('addressee')
            user.uadress = request.POST.get('uadress')
            user.zipcode = request.POST.get('zipcode')
            user.phone = request.POST.get('uphone')
            user.save()
    context = {'tittle':'用户中心','user':user}
    return render(request,'user_manage/user_center_site.html',context)

def base(request):
    context = {'tittle':'base'}
    return render(request,'base.html',context)
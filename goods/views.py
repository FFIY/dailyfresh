from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):

    context = {}
    return render(request,'goods/index.html',context)

def detail(request, goodsid):
    goods = GoodInfo.objects.get(id=goodsid)
    goods.gclick += 1
    goods.save()
    news = goods.gtype.goodinfo_set.order_by('-id')[0:2]

    # 记录用户最近浏览的5条记录
    goods_ids = request.COOKIES.get('goodsids','')
    if goods_ids:
        goods_ids = goodsid
    else:
        goods_ids = goods_ids.split(',')
        if goodsid in goods_ids:
            goods_ids.remove(goodsid)
        goods_ids.insert(0, goodsid)
        if len(goods_ids) > 5:
            goods_ids.pop()
        goods_ids = ','.join(goods_ids)


    context = {'title':goods.gtype.title,'goods':goods,
               'goodsid':goodsid,'news':news,
               }
    response = render(request, 'goods/detail.html', context)
    response.set_cookie('goodsids',goods_ids)
    return response


def list(request, goods_id, curpage, sort):
    goodstype = GoodTypeInfo.objects.get(id=int(goods_id))
    news = goodstype.goodinfo_set.order_by('-id')[0:2]

    if sort == '0': # 默认排序
        goods_list = GoodInfo.objects.filter(gtype_id=int(goods_id)).order_by('-id')
    if sort == '1': # 按价格排序
        goods_list = GoodInfo.objects.filter(gtype_id=int(goods_id)).order_by('-gprice')
    if sort == '3': # 按点击量排序
        goods_list = GoodInfo.objects.filter(gtype_id=int(goods_id)).order_by('-gclick')
    paginator = Paginator(goods_list,10)
    page = paginator.page(int(curpage))
    context = {
        'goods':goods_list,'news':news,'goodstype':goodstype,'page':page,
        'sort':sort, 'paginator':paginator, 'goodstype':goodstype,
        'curpage':curpage,
    }
    return render(request,'goods/list.html',context)


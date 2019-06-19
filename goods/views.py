from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.models import CartInfo

# Create your views here.

def index(request):
    goodtypes = GoodTypeInfo.objects.all()
    typeone = goodtypes[0].goodinfo_set.order_by('-id')[0:4]
    typeone_h = goodtypes[0].goodinfo_set.order_by('-gclick')[0:4]
    typetwo = goodtypes[1].goodinfo_set.order_by('-id')[0:4]
    typetwo_h = goodtypes[1].goodinfo_set.order_by('-gclick')[0:4]
    typethree = goodtypes[2].goodinfo_set.order_by('-id')[0:4]
    typethree_h = goodtypes[2].goodinfo_set.order_by('-gclick')[0:4]
    typefour = goodtypes[3].goodinfo_set.order_by('-id')[0:4]
    typefour_h = goodtypes[3].goodinfo_set.order_by('-gclick')[0:4]
    typefive = goodtypes[4].goodinfo_set.order_by('-id')[0:4]
    typefive_h = goodtypes[4].goodinfo_set.order_by('-gclick')[0:4]
    typesix = goodtypes[5].goodinfo_set.order_by('-id')[0:4]
    typesix_h = goodtypes[5].goodinfo_set.order_by('-gclick')[0:4]

    context = {'title': '首页', 'locals': locals(), 't1': typeone, 't1h': typeone_h, 't2': typetwo, 't2h': typetwo_h,
               't3': typethree, 't3h': typethree_h, 't4': typefour, 't4h': typefour_h, 't5': typefive,
               't5h': typefive_h, 't6h': typesix_h,'t6':typesix,
               }
    return render(request, 'goods/index.html', context)


def detail(request, goodsid):
    print(request.headers.get('Referer'))
    cart_length  = CartInfo.objects.filter(user_id=request.session['user_id']).count()
    goods = GoodInfo.objects.get(id=goodsid)
    goods.gclick += 1
    goods.save()
    news = goods.gtype.goodinfo_set.order_by('-id')[0:2]
    print(news)
    # 记录用户最近浏览的5条记录
    goods_ids = request.COOKIES.get('goodsids','')
    if not goods_ids:
        goods_ids = goodsid
    else:
        goods_ids = goods_ids.split(',')
        if goodsid in goods_ids:
            goods_ids.remove(goodsid)
        goods_ids.insert(0, goodsid)
        if len(goods_ids) > 5:
            goods_ids.pop()
        goods_ids = ','.join(goods_ids)
    print('goods_id',goods_ids)

    context = {'title':goods.gtype.title,'goods':goods,
               'goodsid':goodsid,'news':news,
               'cart_length':cart_length,
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


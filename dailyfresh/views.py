from django.shortcuts import render
from goods.models import *
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
    typefive = goodtypes[3].goodinfo_set.order_by('-id')[0:4]
    typefive_h = goodtypes[3].goodinfo_set.order_by('-gclick')[0:4]
    typesix = goodtypes[3].goodinfo_set.order_by('-id')[0:4]
    typesix_h = goodtypes[3].goodinfo_set.order_by('-gclick')[0:4]

    context = {'title':'首页','locals':locals(),'t1':typeone,'t1h':typeone_h,'t2':typetwo,'t2h':typetwo_h,
               't3':typethree,'t3h':typethree_h,'t4':typefour,'t4h':typefour_h,'th5':typefive,
               'th5h':typefive_h,'th6':typesix_h,
               }
    return render(request, 'goods/index.html', context)
from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    context = {}
    return render(request,'goods/index.html',context)

def detail(request):

    context = {}
    return render(request, 'goods/detail.html',context)


def list(request):

    context = {}
    return render(request,'goods/list.html',context)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
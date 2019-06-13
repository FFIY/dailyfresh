from django.urls import path,re_path
from . import views

urlpatterns =[
    path('',views.index),
    re_path('list/(\d+)-(\d+)-(\d+)',views.list),
    re_path('detail/(\d+)/',views.detail),
]
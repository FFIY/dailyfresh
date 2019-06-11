from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
    path('list/(\d+)-(\d+)-(\d+)',views.list),
    path('detail/(\d+)/',views.detail),
]
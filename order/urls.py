from django.urls import path,re_path
from . import views

urlpatterns =[
    re_path('(\d+)/',views.order),
    path('addorder/',views.order_handle),

]
from django.urls import path,re_path
from . import views

urlpatterns =[
    path('',views.cart),
    re_path('add/(\d+)-(\d+)',views.add),
    re_path('edit/(\d+)-(\d+)/',views.edit),
    re_path('delete/(\d+)/',views.delete)
]
from django.urls import path
from . import views

urlpatterns =[
    path('',views.cart),
    path('add/(\d+)-(\d+)',views.add),

]
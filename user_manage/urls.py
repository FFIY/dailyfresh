from django.urls import re_path,path
from . import views



urlpatterns = [
    path('register/',views.register),
    path('login/',views.login),
    path('register_exist/',views.register_exist),
    path('base/',views.base),
    path('info/',views.info),
    path('order/',views.order),
    path('site/',views.site),
    path('logout/',views.logout),
]
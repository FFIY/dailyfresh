from django.contrib import admin
from .models import GoodTypeInfo,GoodInfo
# Register your models here.

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id','gtitle']

admin.site.register(GoodTypeInfo, TypeInfoAdmin)
admin.site.register(GoodInfo,GoodsInfoAdmin)
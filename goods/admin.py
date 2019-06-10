from django.contrib import admin
from .models import GoodTypeInfo,GoodInfo
# Register your models here.

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id','gtitle']

    class Media:
        js = (
            'plugins/kindeditor/kindeditor-all-min.js',
            'plugins/kindeditor/kindeditor_config.js',
            'plugins/kindeditor/lang/zh-CN.js',
        )


admin.site.register(GoodTypeInfo, TypeInfoAdmin)
admin.site.register(GoodInfo,GoodsInfoAdmin)
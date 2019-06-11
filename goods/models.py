from django.db import models

# Create your models here.
# 商品的分类
class GoodTypeInfo(models.Model):
    # 类的名称
    title = models.CharField(max_length=32)
    isDelete = models.BooleanField(default=0)

    def __str__(self):
        return self.title

class GoodInfo(models.Model):
    #商品的名称
    gtitle = models.CharField(max_length=32)
    gpic = models.ImageField(upload_to='image/goods') # upload_to是什么？
    # 商品价格
    gprice = models.DecimalField(max_digits=6,decimal_places=2)
    #商品的单位
    guntil = models.CharField(max_length=10,default='500g')
    isDelete = models.BooleanField(default=0)
    gclick = models.IntegerField(default=0)
    gintroduction = models.CharField(max_length= 250)
    stock = models.IntegerField(default=0)
    gcontent = models.TextField(blank=True)
    gadv = models.BooleanField(default=0)
    gtype = models.ForeignKey('GoodTypeInfo',on_delete=models.CASCADE)


    def __str__(self):
        return self.gtitle





# class (models.Model):
#     pass
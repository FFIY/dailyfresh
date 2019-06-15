from django.db import models

# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey('user_manage.UserInfo', on_delete=models.CASCADE)
    goods = models.ForeignKey('goods.GoodInfo',on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
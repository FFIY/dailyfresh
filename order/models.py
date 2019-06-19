from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    # 订单号
    oid = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey('user_manage.UserInfo', on_delete=models.CASCADE)
    # 日期
    odate = models.DateTimeField(auto_now=True)
    # 是否完成支付
    oIsPay = models.BooleanField(default=False)
    # 总金额
    ototal = models.DecimalField(max_digits=6,decimal_places=2)
    # 收货地址
    oaddress = models.CharField(max_length=150)

class OrderDetailInfo(models.Model):
    # 商品
    goods = models.ForeignKey('goods.GoodInfo', on_delete= models.CASCADE)
    order = models.ForeignKey('OrderInfo',on_delete= models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    # 商品的信息
    count = models.IntegerField()
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=32,primary_key = True)
    upassword = models.CharField(max_length=30)
    # uadress = models.IntegerField()
    addressee = models.ForeignKey('UserAdress',null=True,on_delete=models.CASCADE)
    phone = models.CharField(max_length=11,default='')
    email= models.CharField(max_length=64)
    # default,blank是python层面的约束不影响数据库

class UserAdress(models.Model):
    r_adress = models.CharField(max_length=100)
    # user = models.ForeignKey('UserInfo',on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=6)
    r_user = models.CharField(max_length=32)
    r_phone = models.CharField(max_length=11,blank=True)
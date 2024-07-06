from django.db import models

# Create your models here.
""" Department Table """
class Department(models.Model):
    id = models.BigAutoField(verbose_name="ID", primary_key=True)
    title = models.CharField(verbose_name= "标题",max_length=32)

""" Staff Table"""
class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    """ 长度为10 小数为2 默认为0 """
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0) 
    create_time = models.DateTimeField(verbose_name="入职时间")

    # MySQL Restriction
    # Non-Restricted Foreign Key
    # depart = models.BigAutoField(verbose_name="部门ID")
    
    # 1. Restricted Foreign Key
    # -to: to which table
    # -to_field: to which field/column
    # 2. digango auto generate an '_id' post_fix for foreign key attributes
    depart = models.ForeignKey(verbose_name="部门ID",to="Department",to_field="id",
                               on_delete=models.SET_NULL, null=True, blank=True)
    
    # Django Restriction
    gender_choices = (
        (1,"男"),
        (2,"女")
        )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)


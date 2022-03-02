from django.contrib.auth.models import AbstractUser
from django.db import models

table_prefix = "lyadmin_"  # 数据库表名前缀

class BaseModel(models.Model):
    """
        基本模型,可直接继承使用，一般不需要使用审计字段的模型可以使用
        覆盖字段时, 字段名称请勿修改
    """
    create_datetime = models.DateTimeField(auto_now=True, null=True, blank=True,verbose_name='创建时间')
    update_datetime = models.DateTimeField(auto_now_add=True,null=True, blank=True, verbose_name='更新时间')

    class Meta:
        abstract = True  # 表示该类是一个抽象类，只用来继承，不参与迁移操作
        verbose_name = '基本模型'
        verbose_name_plural = verbose_name


#自定义

GENDER_CHOICES = (
        (0, "女"),
        (1, "男"),
    )

class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='用户账号', help_text="用户账号")
    email = models.EmailField(max_length=60, verbose_name="邮箱", null=True, blank=True, help_text="邮箱")
    mobile = models.CharField(max_length=11,verbose_name="电话", null=True, blank=True, help_text="电话")
    avatar = models.CharField(max_length=200,verbose_name="头像", null=True, blank=True, help_text="头像")
    name = models.CharField(max_length=40, verbose_name="姓名", help_text="姓名",  null=True)
    nickname = models.CharField(max_length=100, help_text="用户昵称", verbose_name="用户昵称", default="")
    gender = models.IntegerField(choices=GENDER_CHOICES, verbose_name="性别", null=True, blank=True, help_text="性别")

    # 自定义
    class Meta:
        # db_table = table_prefix + "users"
        db_table = "users"
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class ChinaAreas(models.Model):

    adcode = models.CharField(max_length=8, blank=True, null=True)
    level = models.CharField(max_length=16, blank=True, null=True)
    center = models.TextField(blank=True, null=True)  # This field type is a guess.
    centro_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    children_num = models.IntegerField(blank=True, null=True)
    area_name = models.CharField(max_length=32, blank=True, null=True)
    parent_code = models.CharField(max_length=8, blank=True, null=True)
    acroutes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'china_areas'


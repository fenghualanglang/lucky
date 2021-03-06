from django.db import models


class BaseModel(models.Model):
    '''模型抽象基类'''
    gmt_created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    gmt_modified = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        # 说明是一个抽象模型类
        abstract = True


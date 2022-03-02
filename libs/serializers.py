import re
from datetime import datetime


from django.core.mail import send_mail
from django.conf import settings
from django_redis import get_redis_connection
from rest_framework import serializers
from core.models import User, ChinaAreas
from captcha.models import CaptchaStore


class UserSerializer(serializers.Serializer):

    """用户序列化器类"""
    username = serializers.CharField(max_length=16, label='用户名')
    mobile = serializers.CharField(max_length=11, label='昵称')
    introduction = serializers.CharField(max_length=120,  label='昵称', read_only=True)
    gender = serializers.ChoiceField(label='性别', choices=((0, '男'), (1, '女')), default=0, read_only=True)
    birthday = serializers.DateField(label='生日', read_only=True)
    # wechat = serializers.CharField(max_length=255, read_only=True)
    # qq = serializers.CharField(max_length=12, read_only=True)
    # job = serializers.CharField(max_length=12, read_only=True)
    is_active = serializers.ChoiceField(label='激活标志', choices=((0, '未激活'), (1, '已激活')), default=0, read_only=True)
    # dflag = serializers.ChoiceField(label='删除标志', choices=((0, '删除'), (1, '正常')), default=1, read_only=True)
    # status = serializers.ChoiceField(label='状态', choices=((0, '禁用'), (1, '正常')), default=1, read_only=True)
    token = serializers.CharField(label='JWT token', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'username', 'mobile')




class UserSerializer(serializers.Serializer):

    """用户序列化器类"""
    username = serializers.CharField(max_length=16, label='用户名')
    mobile = serializers.CharField(max_length=11, label='昵称')
    introduction = serializers.CharField(max_length=120,  label='昵称', read_only=True)
    gender = serializers.ChoiceField(label='性别', choices=((0, '男'), (1, '女')), default=0, read_only=True)
    birthday = serializers.DateField(label='生日', read_only=True)
    # wechat = serializers.CharField(max_length=255, read_only=True)
    # qq = serializers.CharField(max_length=12, read_only=True)
    # job = serializers.CharField(max_length=12, read_only=True)
    is_active = serializers.ChoiceField(label='激活标志', choices=((0, '未激活'), (1, '已激活')), default=0, read_only=True)
    # dflag = serializers.ChoiceField(label='删除标志', choices=((0, '删除'), (1, '正常')), default=1, read_only=True)
    # status = serializers.ChoiceField(label='状态', choices=((0, '禁用'), (1, '正常')), default=1, read_only=True)
    token = serializers.CharField(label='JWT token', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'username', 'mobile')








# class EmailVerifyRecordSerializer(serializers.ModelSerializer):
#
#     # code = serializers.CharField(max_length=200, label=u"验证码", read_only=True)
#     email = serializers.EmailField(max_length=50, label=u"邮箱", write_only=True)
#
#     class Meta:
#         model = EmailVerifyRecord
#         fields = ('email',)
#
#     def validate_email(self, value):
#         # 邮箱格式
#         if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', value):
#             raise serializers.ValidationError('邮箱格式不正确')
#
#         count = User.objects.filter(email=value).count()
#         if count == 0:
#             raise serializers.ValidationError('邮箱未注册!')
#         return value


# class ResetSerializer(serializers.ModelSerializer):
#
#     password = serializers.CharField(max_length=128, min_length=6, write_only=True)
#     password2 = serializers.CharField(label='重复密码', write_only=True)
#     sign = serializers.CharField(label='重复密码', write_only=True)
#     email = serializers.EmailField(max_length=50, label=u"邮箱", write_only=True)
#
#     class Meta:
#         model = EmailVerifyRecord
#         fields = ('email', 'password', 'password2', 'sign')









# from rest_framework import serializers
# class GoodSerializers(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     ship_free = serializers.BooleanField(default=True)
# class UserSerializers(serializers.Serializer):
#
#     name = serializers.CharField(max_length=30)
#     birthday = serializers.DateField()
#     gender = serializers.CharField(default="female")
#     mobile = serializers.CharField(max_length=11)
#     email = serializers.EmailField(max_length=100)
#     password = serializers.IntegerField(default=0)

# from rest_framework import serializers
# from core.serializers import zjb, LANGUAGE_CHOICES, STYLE_CHOICES
#
#
# class SnippetSerializer(serializers.Serializer):                # 它序列化的方式很类似于Django的forms
#
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})      # style的设置等同于Django的widget=widgets.Textarea
#
#     linenos = serializers.BooleanField(required=False)                          # 用于对浏览器的上的显示
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return zjb.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
#




    # pk = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.CharField(default='python')
    # style = serializers.CharField(default='friendly')
    #
    # def create(self, validated_data):
    #
    #     """如果数据合法就创建并返回一个snippet实例"""
    #     return Article.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #
    #     """如果数据合法就更新并返回一个存在的snippet实例"""
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #
    #     return instance
    #











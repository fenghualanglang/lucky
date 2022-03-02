
from django.urls import path
from django.conf.urls import url, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

from core.api.china_distance import ChinaLocationView
from core.api.user import (
    LoginView,
    RegisterView,

)


schema_view = get_schema_view(
    openapi.Info(
        title="平台API文档",
        default_version='v1',
        # description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    # public 表示文档完全公开, 无需针对用户鉴权
    public=True,
    permission_classes=(permissions.AllowAny,),
    # generator_class=CustomOpenAPISchemaGenerator,
)


urlpatterns = [

    # api文档地址(正式上线需要注释掉)
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #re_path(r'^swagger(?P<format>\.json|\./yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # url(r'^api/v1/goods', GoodsListView.as_view()),

    # 登录的url
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #
    # path('captcha', include('captcha.urls')),
    #
    # url(r'captcha-image', CaptchaView.as_view()),
    #
    # url(r'api/v1/forget', ForgetPwdView.as_view()),
    #
    # url(r'api/v1/reset', ResetView.as_view()),
    #
    # url(r'api/v1/active', ActiveView.as_view()),
    #
    # url(r'api/v1/customer', CustomerUserView.as_view()),


    # 中国
    url(r'api/v1/china/point', ChinaLocationView.as_view(), name='中国 根据位置查坐标   根据坐标查位置'),





    # 前端用户接口
    url(r'api/v1/register/', RegisterView.as_view(), name='前端手机号注册'),
    url(r'api/v1/login', LoginView.as_view(), name='前端登录认证'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


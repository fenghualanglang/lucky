
import re
import json
from uuid import uuid4

import requests
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django_redis import get_redis_connection
from django.contrib.auth import authenticate, logout
from rest_framework.permissions import (IsAuthenticated)
from django.contrib.auth.hashers import make_password

# from libs.serializers import UserSerializers
from rest_framework_jwt.settings import api_settings
from libs.jsonResponse import SuccessResponse, ErrorResponse
from django.core.mail import send_mail
from django.conf import settings
from libs import baseview

from core.models import User, ChinaAreas
from settingConf.constants import ali_district_url
from utils.common import REGEX_MOBILE,get_parameter_dic,ast_convert
from libs.captcha import captcha, jarge_captcha
from libs.util import send_verify_email, decrypt
from utils.search_china import china_location_address, china_location_point


class ChinaLocationView(APIView):

    def get(self, request):
        """
        查询国内
        :param request:
        :return:
        """

        location = request.GET.get('location')
        type = request.GET.get('type', '1')
        if type == '1':
            data = china_location_address(location)
        else:
            data = china_location_point(location)
        return Response({'code': 2000, 'data': data, 'msg': "请求成功"})


#  Atlas 获取全国所有的地理位置信息 指定的城市
"https://geo.datav.aliyun.com/areas_v3/bound/all.json"

class ChinaAreasView(APIView):

    def get(self, request):
        """
        查询中国所有区域
        :param request:
        :return:
        """






class ChinaDistanceView(APIView):

    # permission_classes = ()  # 权限类型
    # authentication_classes = ()  # 身份验证

    def get(self, request):
        """
        查询中国区域 是否包含子节点

        tpye 1 默认包含  其它不包含

        :param request:
        :return:
        """
        location = request.POST.get('location')              # 城市名
        tpye = request.POST.get('location', '1')              # 城市名




    def post(self, request):
        '''
        区域 支持 画圈  支持颜色 线宽的选择

        根据用户输入的城市名： area_name
        根据线段颜色：        line_color
        根据绘画线宽          line_wide
        :param request:
        :return:
        '''
        location = request.POST.get('location')              # 城市名
        line_color = request.POST.get('line_color')          # 线颜色
        line_wide = request.POST.get('line_wide')            # 线宽

        area = ChinaAreas.objects.filter(area_name__icontains=location).first()
        if not area:
            return Response({'code': 4001, 'data': 'data', 'msg': "地点不存在"})


        url = ali_district_url.format("410000")
        res = requests.get(url)
        data = res.json()
        print(res)

        return Response({'code': 2000, 'data': data, 'msg': "请求成功"})






class ChinaPolygonView(APIView):

    # permission_classes = ()  # 权限类型
    # authentication_classes = ()  # 身份验证

    def post(self, request):
        '''
        根据用户输入的城市名： area_name
        根据线段颜色：        line_color
        根据绘画线宽          line_wide
        根据不透明度          polygon_opacity
        根据填充颜色          polygon_fill
        :param request:
        :return:
        '''
        area_name = request.data.get('area_name')            # 城市名
        line_color = request.data.get('line_color')          # 线颜色
        line_wide = request.data.get('line_wide')            # 线宽
        polygon_opacity = request.data.get('line_opacity')   # 线条不透明度
        polygon_fill = request.data.get('polygon_fill')      # 填充颜色

        return Response({'code': 2000, 'data': 'data', 'msg': "请求成功"})



class ChinaFullPolygonView(APIView):

    # permission_classes = ()  # 权限类型
    # authentication_classes = ()  # 身份验证

    def post(self, request):
        '''
        根据用户输入的城市名： area_name
        根据线段颜色：        line_color
        根据绘画线宽          line_wide
        根据不透明度          polygon_opacity
        根据填充颜色          polygon_fill
        :param request:
        :return:
        '''
        area_name = request.data.get('area_name')            # 城市名
        line_color = request.data.get('line_color')          # 线颜色
        line_wide = request.data.get('line_wide')            # 线宽
        polygon_opacity = request.data.get('line_opacity')   # 线条不透明度
        polygon_fill = request.data.get('polygon_fill')      # 填充颜色

        return Response({'code': 2000, 'data': 'data', 'msg': "请求成功"})





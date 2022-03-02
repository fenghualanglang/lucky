import re
import json
from uuid import uuid4

from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django_redis import get_redis_connection
from django.contrib.auth import authenticate, logout
from rest_framework.permissions import (IsAuthenticated)
from django.contrib.auth.hashers import make_password

from rest_framework_jwt.settings import api_settings
from libs.jsonResponse import SuccessResponse, ErrorResponse

from core.models import User
from libs.serializers import (
    UserSerializer,
)
from utils.common import REGEX_MOBILE, get_parameter_dic, ast_convert


class RegisterView(APIView):
    '''
    前端用户注册
    post:
    【功能描述】前端用户注册</br>
    【参数说明】mobile为手机号</br>
    【参数说明】code短信验证码</br>
    【参数说明】password为密码</br>
    【参数说明】password2为确认输入的密码</br>
    '''
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):

        print(request.POST.get('mobile'))

        mobile = request.data.get('mobile')
        code = request.data.get('code')
        password = request.data.get('password')
        password2 = request.data.get('password2')

        if mobile is None or code is None or password is None or password2 is None:
            return ErrorResponse(msg="提交的参数不能为空")

        # 判断密码是否合法
        if len(password) < 6:
            return ErrorResponse(msg="密码长度至少6位")

        if not re.match(r'^[a-zA_Z0-9]{6,20}$', password):
            return ErrorResponse(msg="密码格式不正确(大小写字母、数字组合)")

        if password != password2:
            return ErrorResponse(msg="两次密码输入不一致")

        # 验证手机号是否合法
        if not re.match(REGEX_MOBILE, mobile):
            return ErrorResponse(msg="请输入正确手机号")

        # 判断短信验证码是否正确
        if not re.match(r'^\d{6}$', code):
            return ErrorResponse(msg="验证码格式错误")

        redis_conn = get_redis_connection('verify_codes')

        send_flag = redis_conn.get('sms_%s' % mobile)  # send_flag的值为bytes，需要转换成str ,,send_flag.decode()

        if not send_flag:  # 如果取不到标记，则说明验证码过期
            return ErrorResponse(msg="短信验证码已过期")
        else:
            if str(send_flag.decode()) != str(code):
                return ErrorResponse(msg="验证码错误")
            # 开始注册
            User.objects.create(username=mobile, password=make_password(password), mobile=mobile, is_staff=False)
            return SuccessResponse(msg="注册成功")



class LoginView(APIView):

    # permission_classes = ()  # 权限类型
    # authentication_classes = ()  # 身份验证

    def post(self, request):

        password = request.data.get('password')
        username = request.data.get('username')

        permission = User.objects.filter(username=username).first()
        if permission is None:
            return Response({'code': 4001, 'msg': "账号/密码不正确"})

        # if permission and not permission.is_staff:  # 判断是否允许登录后台
        #     return Response({"code": 4000, "msg": "您没有权限登录后台", "data": None })

        if permission and not permission.is_active:
            return Response({"code": 4000, "msg": "该账号已被禁用,请联系管理员", "data": None })

        if permission and permission.check_password(password):  # check_password() 对明文进行加密,并验证

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 载荷
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            token = jwt_encode_handler(jwt_payload_handler(permission))
            serializer = UserSerializer(permission)

            data = serializer.data
            data.update({"token": token})

            return Response({'code': 2000, 'data': data, 'msg': "请求成功"})

        else:
            return Response({"code": 4000, "msg": "账号/密码不正确", "data": None })








# class RegisterView(APIView):
#
#     permission_classes = ()  # 权限类型
#     authentication_classes = ()  # 身份验证
#
#     def get(self, request):
#
#         return Response({'code': 200, 'data': json.dumps(captcha()), 'msg': 'ok'})
#
#     def post(self, request):
#
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']
#         mobile = serializer.validated_data['mobile']
#         email = serializer.validated_data['email']
#
#         # capt = request.data.get("captcha")
#         # key = request.data.get("hashkey")
#         # if not jarge_captcha(capt, key):
#         #     return Response({'code': 412, 'data': {}, 'msg': '验证码错误'})
#
#         user = User.objects.create_user(
#             username=username,
#             password=password,
#             mobile=mobile,
#             email=email
#         )
#         user.save()
#
#         token = user.generate_active_token()
#
#         msg = f'<a href="{settings.BASE_URL}/active?token={token}" target="_blank">点击激活</a>'
#         send_mail('注册激活', '', settings.EMAIL_FROM, [email], html_message=msg)
#
#         # from celery_tasks.email.tasks import send_verify_email
#         # send_verify_email.delay(email, verify_url)
#         return Response({'code': 200, 'data': {}, 'msg': '用户注册成功,　请前往邮箱激活!'})
#
#
# class ActiveView(APIView):
#
#     permission_classes = ()  # 权限类型
#     authentication_classes = ()  # 身份验证
#
#     def get(self, request):
#         pass
#         # token = request.GET.get('token')
#         #
#         # if token is None:
#         #     return HttpResponse({'code': 400, 'data': {}, 'msg': '缺少token参数'})
#         #
#         # user = User.check_verify_token(token)
#         # if user is None:
#         #     return Response({'code': 400, 'data': {}, 'msg': '无效的token'})
#         #
#         # user.is_active = True
#         # user.save()
#         # return Response({'message': 'OK'})





# class ForgetPwdView(APIView):
#
#     permission_classes = ()  # 权限类型
#     authentication_classes = ()  # 身份验证
#
#     def post(self, request):
#
#         # capt = request.data.get("captcha")
#         # key = request.data.get("hashkey")
#         # if not jarge_captcha(capt, key):
#         #     return Response({'code': 412, 'data': {}, 'msg': '验证码错误'})
#
#         # serializer = EmailVerifyRecordSerializer(data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         # email = serializer.validated_data['email']
#         # send_verify_email('forget', email)
#         #
#         # return Response({'code': 200, 'data': {}, 'msg': '连接已发送邮箱,　请前往邮箱设置!'})
#         pass




# class ResetView(APIView):
#
#     permission_classes = ()  # 权限类型
#     authentication_classes = ()  # 身份验证
#
#     def get(self, request):
#
#         token = request.GET.get('token')
#         data = decrypt(token)
#         if not data:
#             return Response({'code': 412, 'data': {}, 'msg': '链接已过期!'})
#
#         EmailVerifyRecord.objects.filter(email=data.get('email'), send_type=data.get('send_type')).update(sign=str(uuid4()))
#         return Response({'code': 200, 'data': {'sign': str(uuid4())}, 'msg': 'ok'})
#
#     def post(self, request):
#         serializer = ResetSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         email = request.data.get('email')
#         password = request.data.get('password')
#
#         user = User.objects.get(email=email)
#         user.password = make_password(password)
#         user.save()
#         return Response({'code': 200, 'data': {}, 'msg': 'ok!'})
#
#
# class ResetPwd(APIView):
#
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')
#
#         username = request.user.username
#
#         User.objects.filter(username=username, password=old_password).update(password=new_password)
#         return Response({'code': 200, 'data': {}, 'msg': '邮箱地址已更新!'})





class LogoutView(APIView):
    """用户登出"""
    def get(self, request):

        logout(request)
        return Response({'code': 200, 'data': {}, 'msg': '退出登录, 成功!'})








        # # 登录合并购物车
# # POST /authorizations/
# class UserAuthorizeView(ObtainJSONWebToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#
#         if serializer.is_valid():
#             # 账户和密码正确
#             user = serializer.object.get('user') or request.user
#             token = serializer.object.get('token')
#             response_data = jwt_response_payload_handler(token, user, request)
#             response = Response(response_data)
#             if api_settings.JWT_AUTH_COOKIE:
#                 expiration = (datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA)
#                 response.set_cookie(api_settings.JWT_AUTH_COOKIE, token, expires=expiration, httponly=True)
#
#             # 进行购物车记录合并
#             merge_cookie_cart_to_redis(request, user, response)
#             return response
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#







    # def put(self, request, *args, **kwargs):
    #
    #     print(request.user)
    #
    #     if args == 'changepwd':
    #         old_password = request.data.get('old_password')
    #
    #         new_password = request.data.get('new_password')
    #
    #         User.objects.filter(username=request.user, password=old_password).update(password=new_password)
    #
    #         return Response('邮箱地址已更新!')












# ORDER_DICT = {
#     1:{'name':'juzi', 'age': 20, 'sex': 'nam'},
#     2:{'name':'xiangjao', 'age': 20, 'sex': 'nam'},
#     3:{'name':'li', 'age': 20, 'sex': 'nv'},
#     4:{'name':'pingguo', 'age': '20', 'sex': 'nam'},
# }
#
#
# class OrderView(APIView):
#
#     # 引入认证规则局部视图使用，亦可全局使用
#     # authentication_classes = [Authtication]
#     # authentication_classes = [BaseAuthentication]
#
#     # 权限认证
#     permission_classes = [MyPermission]
#
#     def get(self, request, *args, **kwargs):
#
#         # user = request.user
#         # auth = requestuser.auth
#
#         ret = {'code': 1000, 'msg':None, 'date':None}
#         try:
#             ret['date'] = ORDER_DICT
#         except Exception as e:
#             pass
#
#         return JsonResponse(ret)
#
#
#
# class GoodsListView(APIView):
#
#     permission_classes = [MyPermission2]
#     def get(self, request, format=None):
#
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodSerializers(goods, many=True)
#
#         return Response(goods_serializer.data)
#
#
# # # 匿名用户登陆
# class UserInfoView(APIView):
#
#     authentication_classes = []
#     permission_classes = []
#     # throttle_classes = [VisitThrottle]
#
#     def get(self, request, *args, **kwargs):
#         user_info = UserProfile.objects.all()
#         user_info_serializer = UserSerializers(user_info, many=True)
#         return Response(user_info_serializer.data)
#
#
# class LoginView(APIView):
#
#     # 登陆可以不认证，认证为空
#     authentication_classes = []
#     permission_classes = []
#     throttle_classes = []
#
#     def post(self, request, *args, **kwargs):
#
#         username = request._request.POST.get('username')
#         password = request._request.POST.get('password')
#
#         obj = UserInfo.objects.filter(user_name=username, password=password).first()
#
#         if not obj:
#             res = {
#                 'code': '001',
#                 'msg': '用户名或密码错误'}
#             return JsonResponse(res)
#
#         token = token1(username)
#         # 每次登陆更新token功能
#         UserToken.objects.update_or_create(user=obj, defaults={'token':token})
#
#         res = {
#             'code': '001',
#             'token': token}
#         return JsonResponse(res)
#
#
# def token1(user):
#     import hashlib
#     import time
#     ctime = str(time.time())
#
#     m = hashlib.md5(bytes(user, encoding='utf-8'))
#
#     m.update(bytes(ctime, encoding='utf-8'))
#
#     return m.hexdigest()

























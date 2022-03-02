
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# import sys
# sys.path.insert(1, os.path.join(BASE_DIR, 'core'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0cgjo+57we)d&x1kp%@1q8_!^(+si^h%x+)86hqwc9r+@x!qf#'


AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',  # 在线接口文档
    'captcha',
    'core.apps.CoreConfig',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',




]


AUTH_USER_MODEL = "core.User"
ROOT_URLCONF = 'settingConf.urls'
WSGI_APPLICATION = 'settingConf.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "HelloWorld",
        'HOST': '1.116.231.146',
        'PORT': '3306',
        'USER': 'zhangsan',
        'PASSWORD': "Zhangjunbo123@"
    }
}




# 邮件发送设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP服务器地址
EMAIL_HOST = 'smtp.163.com'
# SMTP服务端口
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = 'zhangjunbo0405@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = '1234567qwerty'
# 收件人看到的发件人
EMAIL_FROM = '最上川<zhangjunbo0405@163.com>'

# # 字母验证码
# CAPTCHA_IMAGE_SIZE = (80, 45)  # 设置 captcha 图片大小
# CAPTCHA_LENGTH = 4  # 字符个数
# CAPTCHA_TIMEOUT = 1  # 超时(minutes)
# APTCHA_BACKGROUND_COLOR = '#ffffff'
#
#
# # 加减乘除验证码
# CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
# CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null',  # 没有样式
#                            'captcha.helpers.noise_arcs',  # 线
#                            'captcha.helpers.noise_dots',  # 点
#                            )
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'   # 图片中的文字为随机英文字母，例如mdsh
# # CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# # CAPTCHA_CHALLENGE_FUNCT ='captchachallenge'  #文字为数字表达式，如1 + 2 = </ span>


#字母验证码
CAPTCHA_IMAGE_SIZE = (800, 450)   # 设置 captcha 图片大小
CAPTCHA_LENGTH = 4   # 字符个数
CAPTCHA_TIMEOUT = 10   # 超时(minutes)

#加减乘除验证码
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null',
     'captcha.helpers.noise_arcs', # 线
     'captcha.helpers.noise_dots', # 点
)

# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/STATIC/'



import datetime

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#     ),
#
#     'DEFAULT_PARSER_CLASSES': (
#         'rest_framework.parsers.JSONParser',
#     ),
#
#     # 'DEFAULT_RENDERER_CLASSES': (
#     #     'rest_framework.renderers.JSONRenderer',
#     # )
#
#     # 异常处理
#     'EXCEPTION_HANDLER': 'utils.exceptions.exception_handler',
#
#
# }
JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_response_payload_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3000000),
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True






# 配置redis缓存
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',  # 缓存后端 Redis
        # 连接Redis数据库(服务器地址)
        # 一主带多从(可以配置多个Redis，写走第一台，读走其他的机器)
        'LOCATION': [
            'redis://1.116.231.146:6379/0',
        ],
        'KEY_PREFIX': 'lybbn',  # 项目名当做文件前缀
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',  # 连接选项(默认，不改)
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 512,  # 连接池的连接(最大连接)
            },
            "PASSWORD": "!QAZ2wsx",
        }
    },
    'session': { #缓存session
            'BACKEND': 'django_redis.cache.RedisCache',  # 缓存后端 Redis
            # 连接Redis数据库(服务器地址)
            # 一主带多从(可以配置多个Redis，写走第一台，读走其他的机器)
            'LOCATION': [
                'redis://1.116.231.146:6379/1',
            ],
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',  # 连接选项(默认，不改)
                "PASSWORD": "!QAZ2wsx",
            }
        },
    'verify_codes': { #缓存短信验证码
            'BACKEND': 'django_redis.cache.RedisCache',  # 缓存后端 Redis
            # 连接Redis数据库(服务器地址)
            # 一主带多从(可以配置多个Redis，写走第一台，读走其他的机器)
            'LOCATION': [
                'redis://1.116.231.146:6379/2',
            ],
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',  # 连接选项(默认，不改)
                "PASSWORD": "!QAZ2wsx",
            }
        },
    "carts": { #登陆过的用户购物车的存储
            "BACKEND": "django_redis.cache.RedisCache",
            'LOCATION': [
                'redis://1.116.231.146:6379/3',
            ],
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                'CONNECTION_POOL_KWARGS': {'decode_responses': True}, # 添加这一行,防止取出的值带有b'' bytes
                "PASSWORD": "!QAZ2wsx",
            },
    },
    "authapi": {  # 接口安全校验（验证接口重复第二次访问会拒绝）
            'BACKEND': 'django_redis.cache.RedisCache',  # 缓存后端 Redis
            # 连接Redis数据库(服务器地址)
            # 一主带多从(可以配置多个Redis，写走第一台，读走其他的机器)
            'LOCATION': [
                'redis://1.116.231.146:6379/4',
            ],
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',  # 连接选项(默认，不改)
                "PASSWORD": "!QAZ2wsx",
            }
        },
}



REDIS_TIMEOUT = 7 * 24 * 60 * 60
CUBES_REDIS_TIMEOUT = 60 * 60
NEVER_REDIS_TIMEOUT = 365 * 24 * 60 * 60

# session使用的存储方式
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 指明使用哪一个库保存session数据
SESSION_CACHE_ALIAS = "session"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/crm.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],
            'propagate': True,
        },
    }
}





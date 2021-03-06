from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


# 创建验证码
def captcha():

    hashkey = CaptchaStore.generate_key()  # 验证码答案
    image_url = captcha_image_url(hashkey)  # 验证码地址
    captcha = {'hashkey': hashkey, 'image_url': image_url}

    return captcha

#  验证验证码
def jarge_captcha(captchaStr, captchaHashkey):

    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)

            if get_captcha.response == captchaStr.lower():     # 如果验证码匹配
                return True
        except:
            return False
    else:
        return False
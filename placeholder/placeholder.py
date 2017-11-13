# 配置层
import sys
import os
from django.conf import settings

# 默认为True
DEBUG = os.environ.get('DEBUG', 'on') == 'on'
# 随机生成32位密钥
# SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
SECRET_KEY = os.environ.get('SECRET_KEY', 'eh7)!6iyp@#6g!4q@!!ddo6-&5mjs&ul&jvx+tc7z-&#!gcms+')
# 设置允许请求的域名
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG = DEBUG,
    SECRET_KEY = SECRET_KEY,
    ROOT_URLCONF = __name__,
    ALLOWED_HOSTS = ALLOWED_HOSTS,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

# 视图层
from django import forms
from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from django.conf.urls import url
from io import BytesIO
from PIL import Image, ImageDraw

class ImageForm(forms.Form):
    """用于验证图片的高度和宽度"""

    height = forms.IntegerField(min_value = 1, max_value = 2000)
    width = forms.IntegerField(min_value = 1, max_value = 2000)

    def generate(self, image_format='PNG'):
        """"生成指定类型的图片并以字节形式(二进制)返回"""
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        text = '{} X {}'.format(width, height)
        textwidth, textheight = draw.textsize(text)
        if textwidth < width and textheight < height:
            texttop = (height - textheight) // 2
            textleft = (width - textwidth) // 2
            draw.text((textleft, texttop), text, fill=(255, 255, 255))
        content = BytesIO()
        image.save(content, image_format)
        content.seek(0)
        return content


def palceholder(request, width, height):
    """图片占位视图"""
    form = ImageForm({'heigh': height, 'width': width})
    if forms.is_valid():
        height = forms.cleaned_data['height']
        width = forms.cleaned_data['width']
        return HttpResponse('Ok')
    else:
        return HttpResponseBadRequest('Invalid Image Request')

def index(request):
    """主页视图"""

    return HttpResponse('Hello world')

# url模式
urlpatterns = (
    url(r'^images/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name = 'placeholder'),
    url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

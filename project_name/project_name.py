import sys
import os

from django.conf import settings

# 默认为True
DEBUG = os.environ.get('DEBUG', 'on') == 'on'
# 随机生成32位密钥
# SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')
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

from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application


def index(request):
    return HttpResponse('Hello world')

urlpatterns = (
    url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

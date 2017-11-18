import sys
import os
from django.conf import settings

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

settings.configure(
    DEBUG = True,
    SECRET_KEY = SECRET_KEY,
    ROOT_URLCONF = 'sitebuilder.urls',
    MIDDLEWARE_CLASSES = (),
    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True
        },
    ),
    STATIC_URL='/static/',
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

from django.db import models
from mongoengine import *
from django.conf import settings
from mongotest.settings import DBNAME
# from mongotest.settings import DBNAME
# Create your models here.
connect('comic')
class Pokemon(Document):
    comic_name = StringField()
    number = StringField()
    name_cn = StringField()
    name_jp = StringField()
    name_en = StringField()
    image_dir = StringField()
    google_image_url = StringField()
    page_url = StringField()
    image_urls = StringField()
    meta = {'collection': 'pokemon'}
print(DBNAME)
# for i in Pokemon.objects[:2]:
#     print(i.number)
# pikachu = Pokemon.objects.filter(name_cn='皮卡丘')
# print(pikachu[0].name_en)
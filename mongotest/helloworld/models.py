from django.db import models
from mongoengine import *
from django.conf import settings
# from mongotest.settings import DBNAME
# Create your models here.
# connect('comic')
class Pokemon(Document):
    id = StringField()
    _id = StringField()
    comic_name = StringField()
    number = StringField()
    name_cn = StringField()
    name_jp = StringField()
    name_en = StringField()
    page_url = StringField()
    img_url = StringField()
    meta = {'collection': 'pokemon'}

# for i in Pokemon.objects[:2]:
#     print(i.number)
# pikachu = Pokemon.objects.filter(name_cn='皮卡丘')
# print(pikachu[0].name_en)

# all =  Pokemon.objects.all()
# print(len(all))

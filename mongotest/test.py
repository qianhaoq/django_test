# # use pymongo
# import pymongo
# from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
# db = client.comic

# collections = db.pokemon
# posts = db.posts
# print(db.collection_names())
# print(collections.find_one({"name_cn":"皮卡丘"}))

# use mongoengine
import mongoengine
from mongoengine import *
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

for i in Pokemon.objects[:2]:
    print(i.number)
pikachu = Pokemon.objects.filter(name_cn='皮卡丘')
print(pikachu[0].name_en)
# pikachu = Pokemon.objects.filter(name_cn="皮卡丘")
# print(pikachu.comic_name)
from rest_framework_mongoengine import serializers as mongoserializers
from rest_framework import serializers
from helloworld.models import Pokemon

class PokemonSerilizer(mongoserializers.DocumentSerializer):

    id = serializers.CharField()
    comic_name = serializers.CharField()
    number = serializers.CharField()
    name_cn = serializers.CharField()
    name_jp = serializers.CharField()
    name_en = serializers.CharField()
    page_url = serializers.CharField()
    img_url = serializers.CharField()

    class Meta:
        model = Pokemon
        fields = '__all__'
        # fields = ('number', 'name_cn', 'name_en', 'name_jp')
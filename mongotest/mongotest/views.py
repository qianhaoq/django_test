from django.http import HttpResponse
from helloworld.models import Pokemon
from helloworld.serializer import PokemonSerilizer
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet




def api(request):
    pikachu = Pokemon.objects.filter(name_cn='皮卡丘')
    return HttpResponse(pikachu[0].name_en)
    

def hello(request):
    return HttpResponse("hello mongo")
    # return HttpResponse("mongotest hello world")

class PokemonViewSet(MongoModelViewSet):
    """
    API endpoint that allows pokemon to be viewed
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerilizer
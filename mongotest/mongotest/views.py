from django.http import HttpResponse
from helloworld.models import Pokemon
from helloworld.serializer import PokemonSerilizer
from rest_framework import status, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet


from django_filters.rest_framework import DjangoFilterBackend


def api(request):
    pikachu = Pokemon.objects.filter(name_cn='皮卡丘')
    return HttpResponse(pikachu[0].name_en)
    

def hello(request):
    return HttpResponse("hello mongo")
    # return HttpResponse("mongotest hello world")

from rest_framework_mongoengine.generics import *    
from rest_framework import filters  

class PokemonViewSet(MongoModelViewSet):
    """
    API endpoint that allows pokemon to be viewed
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerilizer
    my_filter_fields = ('id', 'name_cn', 'name_en')
    def get_kwargs_for_filtering(self):
        filtering_kwargs = {} 
        for field in  self.my_filter_fields: # iterate over the filter fields
            field_value = self.request.query_params.get(field) # get the value of a field from request query parameter
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs 

    def get_queryset(self):
        queryset = Pokemon.objects.all() 
        filtering_kwargs = self.get_kwargs_for_filtering() # get the fields with values for filtering 
        if filtering_kwargs:
            queryset = Pokemon.objects.filter(**filtering_kwargs) # filter the queryset based on 'filtering_kwargs'
        return queryset
    # filter_backends = (
    #     DjangoFilterBackend,
    #     filters.SearchFilter,
    #     filters.OrderingFilter,
    # )

    # filter_fields = ('id', 'name_cn', 'name_en')
    # search_fields = ('id', 'name_cn', 'name_en')

from rest_framework_mongoengine.generics import *    
from rest_framework import filters    

class PokemonList(ListCreateAPIView):
    serializer_class = PokemonSerilizer
    my_filter_fields = ('id', 'name_cn', 'name_en') # specify the fields on which you want to filter
    queryset = Pokemon.objects.all() 

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {} 
        for field in  self.my_filter_fields: # iterate over the filter fields
            field_value = self.request.query_params.get(field) # get the value of a field from request query parameter
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs 

    def get_queryset(self):
        queryset = Pokemon.objects.all() 
        filtering_kwargs = self.get_kwargs_for_filtering() # get the fields with values for filtering 
        if filtering_kwargs:
            queryset = Pokemon.objects.filter(**filtering_kwargs) # filter the queryset based on 'filtering_kwargs'
        return queryset

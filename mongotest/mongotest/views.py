from django.http import HttpResponse
from helloworld.models import Pokemon

def hello(request):
    pikachu = Pokemon.objects.filter(name_cn='皮卡丘')
    return HttpResponse(pikachu[0].name_en)
    # return HttpResponse("mongotest hello world")

# def api(request)
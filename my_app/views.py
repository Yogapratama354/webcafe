from django.http import HttpResponse
from django.template import loader

def my_app(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())
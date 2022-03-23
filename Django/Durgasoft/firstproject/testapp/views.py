from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_world_view(request):
    return  HttpResponse('<h1> Hello this is Responce from Django Application</h1>')

# def hello(request):
#     return HttpResponse('<h1> Hello Aditya this is respo. from views of djnago app</h1>')

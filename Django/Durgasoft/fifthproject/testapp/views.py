from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_views(request):
    return HttpResponse('<h1>Response from First views</h1>')


def second_views(request):
    return HttpResponse('<h1>Response from second views</h1>')

def third_views(request):
    return HttpResponse('<h1>Response from third views</h1>')

def fourth_views(request):
    return HttpResponse('<h1>Response from Fourth views</h1>')

def fifth_views(request):
    return HttpResponse('<h1>Response from Fifth views</h1>')


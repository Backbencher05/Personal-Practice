from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def good_morning_view(request):
    return HttpResponse('<h1> hello Friends Good Morning</h1>')

def good_afternoon_view(request):
    return HttpResponse('<h1> hello Friends Good Afternoon</h1>')

def good_evening_view(request):
    return HttpResponse('<h1> hello Friends Good Evening</h1>')


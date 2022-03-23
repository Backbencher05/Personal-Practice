# I have created this file - Aditya

from django.http import HttpResponse


#def index(request):
 #   return HttpResponse('''<h1>Aditya <br> <a href = "https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html">abc</a> <br> 
  #  <a href = "">def</a><br>
   # <a href = "">ghi</a></br>
    #<a href = "">jkl</a>''')


def about(request):
    return HttpResponse("About Aditya")


def index(request):
    return HttpResponse("Hello")


def removepunc(request):
    return HttpResponse("Remove punc")

def capfirst(request):
    return HttpResponse("Capitalize first")

def newlineremove(request):
    return HttpResponse("")

def spaceremove(request):
    return HttpResponse("")

def charcount(request):
    return HttpResponse("")
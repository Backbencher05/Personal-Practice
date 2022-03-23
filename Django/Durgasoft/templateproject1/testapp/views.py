from django.shortcuts import render
# from django.http import HttpResponse
import datetime

# Create your views here.


def template_view(request):
    dt = datetime.datetime.now()

    name = 'Aditya'
    rollno = 101
    marks = 100
    my_dict = {}
    #my_dict = {'date': dt}     
    #return render(request, 'testapp/results.html', context=my_dict)     
    return render(request, 'testapp/results.html', {'date': dt})
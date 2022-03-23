from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def emp_data_view(request):
    emp_data ={
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }

    resp = '<h1>Employee Number: {}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(emp_data['eno'], emp_data['ename'], emp_data['esal'],emp_data['eaddr'],)

    return HttpResponse(resp)


import json

def emp_data_jsonview(request):
    # this is python dictionary
    emp_data ={
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }

    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type = 'application/json')




from django.http import JsonResponse

def emp_data_jsonview2(request):
# this is python dictionary
    emp_data ={
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }
    return JsonResponse(emp_data)








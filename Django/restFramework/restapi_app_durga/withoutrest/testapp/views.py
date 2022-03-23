from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 1. first way , it respose http way
def emp_data_view(request):
    emp_data = {
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000, 
        'eaddr': 'Mumbai',
    }
    resp = '<h1>Employee Number: {}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'],)
    return HttpResponse(resp)


import json
def emp_data_jsonview(request):
    # this is python dictionary
    emp_data = {
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type= 'application/json')

    #resp = '<h1>Employee Number: {}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'],)
    #return HttpResponse(resp)


from django.http import JsonResponse

def emp_data_jsonview2(request):
    # this is python dictionary
    emp_data = {
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }
    #json_data = json.dumps(emp_data)
    return JsonResponse(emp_data)

from django.views.generic import View

class JsonCBV(View):
    def get(self,request,*args, **kwargs):
        json_data = json.dumps({'msg': 'This is from get method'})
        return HttpResponse(json_data, content_type = 'application/jon')

    def post(self,request,*args, **kwargs):
        json_data = json.dumps({'msg': 'This is from post method'})
        return HttpResponse(json_data, content_type = 'application/jon')

    def put(self,request,*args, **kwargs):
        json_data = json.dumps({'msg': 'This is from put method'})
        return HttpResponse(json_data, content_type = 'application/jon')

    def delete(self,request,*args, **kwargs):
        json_data = json.dumps({'msg': 'This is from delete method'})
        return HttpResponse(json_data, content_type = 'application/jon')




    

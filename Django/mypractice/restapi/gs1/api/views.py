#from restapi.gs1.api.models import Student
#from restapi.gs1.api import serializers
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

# to get all the information 

def Student_list_view(request):
    stu = Student.objects.all()  # complex data aa gya  (all data)
    print("fist")
    print(stu)
    serializer = StudentSerializer(stu, many=True) # complex data ka python me convert krr lia
    print("second")
    print(serializer)
    print("third")
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data) # now python data ko render krr dia to vo json me convert ho gya
    print("fourth")
    print(json_data)
    return HttpResponse(json_data, content_type='application/json') # json  data ko return krr lia 


# to get specific information
def Student_all_details_view(request):
    stu= Student.objects.get(id=2)  # now here i only want data of table(complex data whoose id is 2)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')

# let make it paramiterised

def Student_specific(request, pk):
    stu = Student.objects.get(id = pk)
    serializer= StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
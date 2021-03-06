from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
def student_details(request):
    stu = Student.objects.get(id = 2)
    #print(stu)
    serializer = StudentSerializers(stu)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    

def student_list(request):
    stu = Student.objects.all( )
    #print(stu)
    serializer = StudentSerializers(stu, many = True)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data, content_type='application/json')
from django.shortcuts import render
from api.models import Student
from api.serialisations import StudentSerialiser
from django.http import HttpResponse , JsonResponse

# Create your views here.

def student_view(request):
    stu = Student.objects.get(id = 2)
    serialiser = StudentSerialiser(stu)
    return JsonResponse(serialiser.data)

def stu(request):
    stu = Student.objects.all()
    serialiser = StudentSerialiser(stu, many= True)
    return JsonResponse(serialiser.data)



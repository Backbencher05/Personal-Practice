from models_pract.testapp.models import Employee
from django.shortcuts import render

# Create your views here.

def employee_views(request):
    employee = Employee.objects.all()
    return render

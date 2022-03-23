from django.shortcuts import render

from testapp.models import Employee

# Create your views here.

def empl_info_view(request):
    employee = Employee.objects.all()
    return render(request, )
    
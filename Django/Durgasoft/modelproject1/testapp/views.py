from testapp.models import Employee
from django.shortcuts import render

# Create your views here.
def employee_info_view(request):
    employees = Employee.objects.all()
    return render(request, 'testapp/results.html', {'employees': employees})
      
    


from django.shortcuts import render
from enroll.form import StudentRegistration


# Create your views here.
def showformdata(request):
    fm = StudentRegistration()
    return render(request, 'enroll/ureg.html', {'form': fm})
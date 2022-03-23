from django.contrib import admin
from testapp.models import Employee
from testapp.models import Jobmodel
from testapp.models import Books
from testapp.models import Costomer
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin): 
    list_display = ['id','eno', 'ename', 'esal', 'eaddr']

class JobAdmin(admin.ModelAdmin):
    list_display = ['posting_date', 'location', 'offered_salary','Qualification']

   



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Jobmodel, JobAdmin)
admin.site.register(Books)
admin.site.register(Costomer)
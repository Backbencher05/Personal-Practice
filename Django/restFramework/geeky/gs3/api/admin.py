from django.contrib import admin
from django.db import models
from api.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'addr']


admin.site.register(Student, StudentAdmin)

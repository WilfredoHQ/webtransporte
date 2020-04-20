from django.contrib import admin
from .models import Employee

# Register your models here.

class AdminEmployee(admin.ModelAdmin):
    list_display = ['__str__', 'job', 'description']


admin.site.register(Employee, AdminEmployee)
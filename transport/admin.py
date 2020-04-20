from django.contrib import admin
from .models import Cooperative, City, Travel, Schedule

# Register your models here.

class AdminCooperative(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'fax', 'mail']


class AdminTravel(admin.ModelAdmin):
    list_display = ['__str__', 'origin', 'route', 'destination', 'price', 'isactive']


class AdminSchedule(admin.ModelAdmin):
    list_display = ['__str__', 'hour']

admin.site.register(Cooperative, AdminCooperative)
admin.site.register(City)
admin.site.register(Travel, AdminTravel)
admin.site.register(Schedule, AdminSchedule)
from django.contrib import admin
from .models import Cooperative, City, Travel, Schedule

# Register your models here.

admin.site.register(Cooperative)
admin.site.register(City)
admin.site.register(Travel)
admin.site.register(Schedule)
from django.views.generic.list import ListView
from .models import Employee

# Create your views here.

class AboutListView(ListView):
    model = Employee
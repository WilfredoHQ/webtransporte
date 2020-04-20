from django.views.generic.list import ListView
from .models import Cooperative

# Create your views here.

class DirectoryListView(ListView):
    model = Cooperative
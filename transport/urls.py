from django.urls import path

from .views import DirectoryListView

urlpatterns = [
    path('', DirectoryListView.as_view() , name='directory'),
]
from django.urls import path

from .views import DirectoryPageView

urlpatterns = [
    path('', DirectoryPageView.as_view() , name='directory'),
]
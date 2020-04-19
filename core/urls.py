from django.urls import path

from .views import HomePageView, DirectoryPageView, AboutPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view() , name='home'),
    path('directory/', DirectoryPageView.as_view() , name='directory'),
    path('about/', AboutPageView.as_view() , name='about'),
    path('contact/', ContactPageView.as_view() , name='contact'),
]
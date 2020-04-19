from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/home.html"


class ContactPageView(TemplateView):
    template_name = "core/contacto.html"
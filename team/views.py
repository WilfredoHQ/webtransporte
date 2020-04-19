from django.views.generic.base import TemplateView

# Create your views here.

class AboutPageView(TemplateView):
    template_name = "core/nosotros.html"
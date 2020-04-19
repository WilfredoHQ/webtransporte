from django.views.generic.base import TemplateView

# Create your views here.

class DirectoryPageView(TemplateView):
    template_name = "core/directorio.html"
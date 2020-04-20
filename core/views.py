from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from transport.models import Cooperative, City, Travel, Schedule

from django.http import JsonResponse

# Create your views here.

class HomePageView(ListView):
    model = Travel
    template_name = 'core/travel_list.html'

    def get_queryset(self):
        origin = self.request.GET.get('origin')
        destination = self.request.GET.get('destination')
        new_context = Travel.objects.filter(
            origin_id=origin, destination_id=destination,
        )
        return new_context

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['cities'] = City.objects.all()
        context['schedule'] = Schedule.objects.all()
        return context


class ContactPageView(TemplateView):
    template_name = "core/contacto.html"

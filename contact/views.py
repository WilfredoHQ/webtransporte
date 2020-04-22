from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm

# Create your views here.

class ContactPageView(FormView):
    template_name = "contact/contacto.html"
    form_class = ContactForm
    success_url = '?ok'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()

        if form.is_valid():
            name = self.request.POST.get('name', '')
            email = self.request.POST.get('email', '')
            case = self.request.POST.get('case', '')
            content = self.request.POST.get('content', '')

        return super().form_valid(form)

    
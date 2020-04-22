from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

class ContactPageView(FormView):
    template_name = "contact/contacto.html"
    form_class = ContactForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()

        if form.is_valid():
            name = self.request.POST.get('name', '')
            email = self.request.POST.get('email', '')
            case = self.request.POST.get('case', '')
            content = self.request.POST.get('content', '')

            # Enviamos el correo

            email = EmailMessage(
                "Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["wilfredo_sj@hotmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                self.success_url = '?ok'
            except:
                self.success_url = '?fail'

        return super().form_valid(form)

    
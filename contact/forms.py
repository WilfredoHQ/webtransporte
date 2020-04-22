from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'class': 'form-control required name', 'placeholder': 'Ingrese su nombre'}), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control required email', 'placeholder': 'Ingrese su correo electrónico'}), min_length=3, max_length=100)
    case = forms.CharField(label='Asunto', required=True, widget=forms.TextInput(attrs={'class': 'form-control required', 'placeholder': 'Asunto...'}), min_length=3, max_length=100)
    content = forms.CharField(label='Mensaje' , required=True, widget=forms.Textarea(attrs={'class': 'form-control required', 'rows': 5, 'placeholder': 'Mensaje...'}), min_length=3, max_length=1000)
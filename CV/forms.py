from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Correo Electrónico')
    subject = forms.CharField(max_length=100, label='Asunto')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')

from django.conf import settings
from django.template import loader
from django.core.mail import send_mail
from django import forms

from .models import Contact




class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        widgets = {
            'name': forms.TextInput(),
            'company': forms.TextInput,
            'email': forms.EmailInput(attrs={'placeholder': 'Important! We need this to contact you.'}),
            'phone_number': forms.TextInput(),
           
            'message': forms.Textarea(attrs={'placeholder': 'Tell us about yourself', 'rows': '5'}),
           
        }

    def save(self, commit=True):
        instance = super(ContactForm, self).save(commit=commit)

        send_mail('A new email from your site!', instance.name + "   " + instance.email + "    from company:" + instance.company + " sent you this message:    " + instance.message + "phone number: " +instance.phone_number , 'madeup@gmail.com', ['msgcommunications@gmail.com'], fail_silently=False)
      
        return instance
from django import forms
from django.forms import inlineformset_factory
from .models import Contact, ContactNumber


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'company']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company (optional)'}),
        }

    ContactNumberFormset = inlineformset_factory(Contact, ContactNumber, fields=('number', 'type'), extra=1,
                                                 can_delete=True, widgets={
            'number': forms.TextInput(attrs={'placeholder': 'Number'}),
            'type': forms.Select(attrs={'class': 'select'}),
        })

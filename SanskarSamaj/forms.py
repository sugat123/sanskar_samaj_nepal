from SanskarSamaj.models import *
from django import forms

from admin.models import ContactForm, VolunteerForm


class CForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'message']


class VForm(forms.ModelForm):
    class Meta:
        model = VolunteerForm
        fields = ['name', 'email', 'message']



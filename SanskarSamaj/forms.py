from SanskarSamaj.models import *
from django import forms

class VForm(forms.ModelForm):
    class Meta:
        model = VolunteerForm
        fields = ['name', 'email', 'message']

class CForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email','subject', 'message']

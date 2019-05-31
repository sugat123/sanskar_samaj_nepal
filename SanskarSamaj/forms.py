<<<<<<< HEAD
from SanskarSamaj.models import *
from django import forms

from admin.models import ContactForm, VolunteerForm


class CForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email','subject', 'message']

class VForm(forms.ModelForm):
    class Meta:
        model = VolunteerForm
        fields = ['name', 'email', 'message']


=======
>>>>>>> 5876d6d9c416c6563d6cae6aa661b3c3f77334be

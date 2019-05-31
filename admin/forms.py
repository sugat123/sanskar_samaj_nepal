from django import forms

from admin.models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = '__all__'

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class AddCauseForm(forms.ModelForm):
    class Meta:
        model = Cause
        fields = '__all__'

class AddTestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'

class AddGalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


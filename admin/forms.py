from django import forms

from admin.models import *



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SectionComponentForm(forms.ModelForm):
    class Meta:
        model = SectionComponent
        fields = '__all__'


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'


class AddBannerForm(forms.ModelForm):
    class Meta:
        model = Banner
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

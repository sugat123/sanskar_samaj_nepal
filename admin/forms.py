from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ImageField

from admin.models import *



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)


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
        exclude = ['views']


class AddCauseForm(forms.ModelForm):
    class Meta:
        model = Cause
        exclude = ['views']


class AddTestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'


class AddGalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        exclude = ['views']

class MoreImageForm(forms.ModelForm):
    class Meta:
        model = MoreImage
        fields = '__all__'
        
class SendMailContact(forms.Form):
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)

class SendMailVolunteer(forms.Form):

    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)


class AddUserForm(UserCreationForm):
   
    
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')
        return email

    class Meta:
        model = User
        fields = [ 'username', "email", "password1", "password2", 'is_superuser']


class EditUserForm(forms.ModelForm):
    
    def clean_email(self):
        email = self.cleaned_data['email']
        email_exists = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if self.instance and self.instance.pk and not email_exists:
            return email

        return email

    class Meta:
        model = User
        fields = [ 'username', "email", 'is_superuser', 'is_active']

class AddEmail(forms.ModelForm):
    class Meta:
        model = EmailToReceive
        fields = '__all__'

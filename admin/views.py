from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from admin.models import *

from admin.forms import *


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # remember_me = form.cleaned_data['remember_me']
            user = authenticate(request, username=username, password=password)
            if user and user.is_superuser:
                login(request, user)
                # if not remember_me:
                #     request.session.set_expiry(0)
                redirect_url = request.GET.get('next', 'admin:dashboard')
                messages.success(request, 'logged in.')
                return redirect(redirect_url)
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'admin/index.html', {'form': form})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'logged out successfully')
        return redirect('/')

def dashboard(request):
    return render(request, 'admin/dashboard.html', {})

def view_setting(request):
    
    return render(request, 'admin/view_setting.html', {})

def edit_setting(request):
    settings = Setting.objects.all().order_by('-date')
    if request.method == 'POST':
        form = SettingForm(request.POST or None)
        if form.is_valid():
            setting = form.save(commit=False)
            setting.save()
            messages.success(request,' Settings updated.')
            return redirect('admin:edit_setting')
    else:
        form = SettingForm()
    return render(request, 'admin/edit_setting.html', {'form':form, 'settings':settings})

def view_banner(request):
    return render(request, 'admin/view_banner.html', {})

def edit_banner(request):
    return render(request, 'admin/edit_banner.html', {})

def view_event(request):
    events = Event.objects.all().order_by('-auto_date')
    return render(request, 'admin/view_event.html', {'events':events})

def add_event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST or None)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            messages.success(request,' Event added.')
            return redirect('admin:add_event')
    else:
        form = AddEventForm()
    return render(request, 'admin/add_event.html', {'form':form})

def view_cause(request):
    causes = Cause.objects.all.order_by('-date')
    return render(request, 'admin/view_cause.html', {'causes':causes})

def add_cause(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST or None)
        if form.is_valid():
            cause = form.save(commit=False)
            cause.save()
            messages.success(request,' Cause added.')
            return redirect('admin:add_cause')
    else:
        form = AddCauseForm()
    return render(request, 'admin/add_cause.html', {'form':form})

def view_gallery(request):
    return render(request, 'admin/view_gallery.html', {})

def add_gallery(request):
    return render(request, 'admin/add_gallery.html', {})

def view_testimonial(request):
    return render(request, 'admin/view_testimonial.html', {})

def add_testimonial(request):
    return render(request, 'admin/add_testimonial.html', {})

def contact_message(request):
    return render(request, 'admin/contact_message.html', {})

def volunteer_message(request):
    return render(request, 'admin/volunteer_message.html', {})



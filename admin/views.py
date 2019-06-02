from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from admin.models import *
from SanskarSamaj.views import contact_page
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
    details = Detail.objects.all()
    settings = SectionComponent.objects.all()
    return render(request, 'admin/view_setting.html', {'settings': settings, 'details': details})


def edit_setting(request, id):
    setting = get_object_or_404(SectionComponent, id=id)
    if request.method == 'POST':
        form = SectionComponentForm(request.POST or None, request.FILES or None, instance=setting)
        if form.is_valid():
            setting = form.save(commit=False)
            setting.save()
            messages.success(request, ' Updated.')
            return redirect('admin:view_setting')

    return render(request, 'admin/edit_setting.html', {'setting': setting})


def edit_detail(request, id):
    detail = get_object_or_404(Detail, id=id)
    if request.method == 'POST':
        form = DetailForm(request.POST or None, instance=detail)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.save()
            messages.success(request, 'Updated.')
            return redirect('admin:view_setting')

    return render(request, 'admin/edit_detail.html', {'detail': detail})


def add_setting(request):
    if request.method == 'POST':
        form = SectionComponentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            setting = form.save(commit=False)
            setting.save()

            return redirect('admin:view_setting')
    else:
        form = SectionComponentForm()
    return render(request, 'admin/add_setting.html', {'form': form})


def add_detail(request):
    if request.method == 'POST':
        form = DetailForm(request.POST or None)
        if form.is_valid():
            setting = form.save(commit=False)
            setting.save()

            return redirect('admin:view_setting')
    else:
        form = DetailForm()
    return render(request, 'admin/add_detail.html', {'form': form})


def add_banner(request):
    if request.method == "POST":
        form = AddBannerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('admin:view_banner')
    else:
        form = AddBannerForm()
    return render(request, 'admin/add_banner.html', {'form': form})


def view_banner(request):
    banners = Banner.objects.all()
    return render(request, 'admin/view_banner.html', {'banners': banners})


def edit_banner(request, id):
    banner = get_object_or_404(Banner, id=id)
    if request.method == "POST":
        form = AddBannerForm(request.POST or None, request.FILES or None, instance=banner)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('admin:view_banner')
    return render(request, 'admin/edit_banner.html', {'banner': banner})


def view_event(request):
    events = Event.objects.all().order_by('-auto_date')
    return render(request, 'admin/view_event.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            messages.success(request, ' Event added.')
            return redirect('admin:add_event')
    else:
        form = AddEventForm()
    return render(request, 'admin/add_event.html', {'form': form})


def edit_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    if request.method == 'POST':

        form = AddEventForm(request.POST or None, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            messages.success(request, ' Event  updated.')
            return redirect('admin:view_event')
    else:
        form = AddEventForm()

    return render(request, 'admin/edit_event.html', {'event': event, 'form': form})


def delete_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    event.delete()
    messages.success(request, '{} Event deleted'.format(event.title))
    return redirect('admin:view_event')


def detail_event(request, slug):
    event = get_object_or_404(Event, slug=slug)

    return render(request, 'admin/detail_event.html', {'event': event})


def view_cause(request):
    causes = Cause.objects.all().order_by('-date')
    return render(request, 'admin/view_cause.html', {'causes': causes})


def add_cause(request):
    if request.method == 'POST':
        form = AddCauseForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            cause = form.save(commit=False)
            cause.save()
            messages.success(request, ' Cause added.')
            return redirect('admin:add_cause')
    else:
        form = AddCauseForm()
    return render(request, 'admin/add_cause.html', {'form': form})


def edit_cause(request, slug):
    cause = get_object_or_404(Cause, slug=slug)
    if request.method == 'POST':

        form = AddCauseForm(request.POST or None, instance=cause)
        if form.is_valid():
            cause = form.save(commit=False)
            cause.save()
            messages.success(request, ' Cause  updated.')
            return redirect('admin:view_cause')
    else:
        form = AddCauseForm()

    return render(request, 'admin/edit_cause.html', {'cause': cause, 'form': form})


def delete_cause(request, slug):
    cause = get_object_or_404(Cause, slug=slug)
    cause.delete()
    messages.success(request, '{} Cause deleted'.format(cause.title))
    return redirect('admin:view_cause')


def detail_cause(request, slug):
    cause = get_object_or_404(Cause, slug=slug)

    return render(request, 'admin/detail_cause.html', {'cause': cause})


def view_gallery(request):
    gallerys = Gallery.objects.all().order_by('-date')
    return render(request, 'admin/view_gallery.html', {'gallerys': gallerys})


def add_gallery(request):
    if request.method == 'POST':
        form = AddGalleryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery = form.save(commit=False)
            gallery.save()
            messages.success(request, ' Image added.')
            return redirect('admin:add_gallery')
    else:
        form = AddGalleryForm()
    return render(request, 'admin/add_gallery.html', {'form': form})


def edit_gallery(request, slug):
    gallery = get_object_or_404(Gallery, slug=slug)
    if request.method == 'POST':

        form = AddGalleryForm(request.POST or None, instance=gallery)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.save()
            messages.success(request, ' Gallery  updated.')
            return redirect('admin:view_gallery')
    else:
        form = AddGalleryForm()

    return render(request, 'admin/edit_gallery.html', {'gallery': gallery, 'form': form})


def delete_gallery(request, slug):
    gallery = get_object_or_404(Gallery, slug=slug)
    gallery.delete()
    messages.success(request, '{} image deleted'.format(gallery.image_title))
    return redirect('admin:view_gallery')


def detail_gallery(request, slug):
    gallery = get_object_or_404(Gallery, slug=slug)

    return render(request, 'admin/detail_gallery.html', {'gallery': gallery})


def view_testimonial(request):
    testimonials = Testimonial.objects.all().order_by('-date')
    return render(request, 'admin/view_testimonial.html', {'testimonials': testimonials})


def add_testimonial(request):
    if request.method == 'POST':
        form = AddTestimonialForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.save()
            messages.success(request, ' Testimonial added.')
            return redirect('admin:add_testimonial')
    else:
        form = AddTestimonialForm()
    return render(request, 'admin/add_testimonial.html', {'form': form})


def edit_testimonial(request, slug):
    testimonial = get_object_or_404(Testimonial, slug=slug)
    if request.method == 'POST':

        form = AddTestimonialForm(request.POST or None, instance=testimonial)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.save()
            messages.success(request, ' Testimonial  updated.')
            return redirect('admin:view_testimonial')
    else:
        form = AddTestimonialForm()

    return render(request, 'admin/edit_testimonial.html', {'testimonial': testimonial, 'form': form})


def delete_testimonial(request, slug):
    testimonial = get_object_or_404(Testimonial, slug=slug)
    testimonial.delete()
    messages.success(request, '{}  deleted'.format(testimonial.title))
    return redirect('admin:view_testimonial')


def detail_testimonial(request, slug):
    testimonial = get_object_or_404(Testimonial, slug=slug)

    return render(request, 'admin/detail_testimonial.html', {'testimonial': testimonial})


def contact_message(request):
    contacts = ContactForm.objects.all().order_by('-date')
    return render(request, 'admin/contact_message.html', {'contacts': contacts})


def volunteer_message(request):
    volunteers = VolunteerForm.objects.all().order_by('-date')
    return render(request, 'admin/volunteer_message.html', {'volunteers': volunteers})


from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from SanskarSamaj.forms import CForm, VForm
from admin.models import Testimonial, Cause, Banner, Gallery, Event, VolunteerForm, MoreImage, SectionComponent, Detail


def index(request):
    banners = Banner.objects.all()
    causes = Cause.objects.all()
    testimonials = Testimonial.objects.order_by('-pk')[0:2]
    galleries = Gallery.objects.order_by('-pk')[0:12]
    events = Event.objects.all().order_by('date')
    latest_event = Event.objects.order_by('-pk')[0:6]
    latest_event2 = Event.objects.order_by('-pk')[0:2]
    context = {
        'banners': banners,
        'causes': causes,
        'testimonials': testimonials,
        'galleries': galleries,
        'events': events,
        'latest_event': latest_event,
        'latest_event2': latest_event2,

    }
    return render(request, 'SanskarSamaj/index.html', context)


def gallery(request):
    galleries = Gallery.objects.all().order_by('-date')
    banner = Banner.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(galleries, 9)
    try:
        galleries = paginator.page(page)
    except PageNotAnInteger:
        galleries = paginator.page(1)
    except EmptyPage:
        galleries = paginator.page(paginator.num_pages)

    context = {
        'galleries': galleries,
        'banner': banner,

    }
    return render(request, 'SanskarSamaj/gallery.html', context)


def gallery_detail(request, slug):
    gallerys = Gallery.objects.all().order_by('-date')
    gallery = Gallery.objects.get(slug=slug)
    gallery.views += 1
    gallery.save()
    banner = Banner.objects.all()

    more_images = MoreImage.objects.filter(image_title_id=gallery)

    context = {
        'gallery': gallery,
        'gallerys': gallerys,
        'more_images': more_images,
        'banner': banner,

    }
    return render(request, 'SanskarSamaj/gallery_detail.html', context)


def causes_page(request):
    cause = Cause.objects.all().order_by('date')
    banner = Banner.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(cause, 6)
    try:
        cause = paginator.page(page)
    except PageNotAnInteger:
        cause = paginator.page(1)
    except EmptyPage:
        cause = paginator.page(paginator.num_pages)

    context = {
        'cause': cause,

        'banner': banner,

    }
    return render(request, 'SanskarSamaj/causes.html', context)


def causes_detail(request, slug):
    cause = Cause.objects.get(slug=slug)
    cause.views += 1
    cause.save()
    causes = Cause.objects.all()
    banner = Banner.objects.all()
    context = {
        'cause': cause,
        'banner': banner,
        'causes': causes

    }
    return render(request, 'SanskarSamaj/causes_detail.html', context)


def volunteer_page(request):
    banner = Banner.objects.all()
    context = {

        'banner': banner,
    }
    return render(request, 'SanskarSamaj/volunteer.html', context)


def contact_page(request):
    banner = Banner.objects.all()
    latest_event2 = Event.objects.order_by('-pk')[0:2]
    if request.method == 'POST':
        form = CForm(request.POST)
        form2 = VForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = "{0} with email address {1} has sent you new message \n\n{2}".format(name, email,
                                                                                           form.cleaned_data['message'])

            form.save(commit=False)
            send_mail(name, message, 'Sanskar Samaj <settings.EMAIL_HOST_USER>', ['sugatp454@gmail.com'])
            form.save()
            messages.success(request, 'Success')
            return redirect('contact_page')
        elif form2.is_valid():
            form2.save(commit=False)
            form2.save()
            messages.success(request, 'Success')
            return redirect('volunteer_page')
    else:
        form = CForm()
        form2 = VForm()
    context = {

        'form': form,
        'form2': form2,

        'latest_event2': latest_event2,
        'banners': banner,
    }
    return render(request, 'SanskarSamaj/contact.html', context)


def about_page(request):
    banners = Banner.objects.all()
    testimonial = Testimonial.objects.order_by('-pk')[0:2]
    latest_event2 = Event.objects.order_by('-pk')[0:2]

    context = {
        'testimonial': testimonial,
        'latest_event2': latest_event2,
        'banners': banners
    }

    return render(request, 'SanskarSamaj/about.html', context)


def events_page(request):
    event = Event.objects.all().order_by('-date')
    banner = Banner.objects.all()
    latest_event2 = Event.objects.order_by('-pk')[0:2]
    page = request.GET.get('page', 1)
    paginator = Paginator(event, 6)
    try:
        event = paginator.page(page)
    except PageNotAnInteger:
        event = paginator.page(1)
    except EmptyPage:
        event = paginator.page(paginator.num_pages)

    context = {
        'event': event,

        'latest_event2': latest_event2,
        'banner': banner,

    }
    return render(request, 'SanskarSamaj/events.html', context)


def events_detail(request, slug):
    event = Event.objects.get(slug=slug)
    event.views += 1
    event.save()
    banner = Banner.objects.all()
    events = Event.objects.all()
    latest_event2 = Event.objects.order_by('-pk')[0:2]
    context = {
        'event': event,
        'events': events,
        'latest_event2': latest_event2,
        'banner': banner,

    }
    return render(request, 'SanskarSamaj/events_detail.html', context)

# def handler404(request):
#     return render(request, 'SanskarSamaj/404.html', status = 404)

# def handler500(request):
#     return render(request, 'SanskarSamaj/500.html', status = 500)

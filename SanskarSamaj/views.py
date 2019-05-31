from django.shortcuts import render, redirect, render_to_response
from SanskarSamaj.models import *
from SanskarSamaj.forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.template import RequestContext
# from SanskarSamaj.context_processor import volunteer_page2



from admin.models import Banner, Causes, Testimonial, Gallery, Event, MoreImage


def index(request):
    banner = Banner.objects.all()
    cause = Causes.objects.all()
    testimonial = Testimonial.objects.order_by('-pk')[0:2]
    gallery = Gallery.objects.order_by('-pk')[0:12]
    events = Event.objects.all().order_by('date')
    latest_event = Event.objects.order_by('-pk')[0:6]
    latest_event2 = Event.objects.order_by('-pk')[0:2]
    volunteer = Volunteer.objects.all().order_by('date')

    if request.method == 'POST':
        form = VForm(request.POST)
        if form.is_valid():
            form.save(commit = False)
            form.save()
            messages.success(request, 'Success')
            return redirect('volunteer_page')
        else:
             messages.error(request, "Sorry try again")
    else:
        form = VForm()


    context = {
        'banner': banner,
        'cause': cause,
        'testimonial': testimonial,
        'gallery': gallery,
        'events': events,
        'latest_event': latest_event,
        'latest_event2': latest_event2


    }
    return render(request, 'SanskarSamaj/index.html', context)

def gallery(request):
    gallery = Gallery.objects.filter(active = True).order_by('-date')
    banner = Banner.objects.all()
    # volunteer = Volunteer.objects.all().order_by('-date')
    # nav = Nav.objects.all()
    # footer = Footer.objects.all()
    # about = About.objects.all()
    # latest_event2 = Events.objects.order_by('-pk')[0:2]

    page = request.GET.get('page', 1)
    paginator = Paginator(gallery, 9)
    try:
        gallery = paginator.page(page)
    except PageNotAnInteger:
        gallery = paginator.page(1)
    except EmptyPage:
        gallery = paginator.page(paginator.num_pages)

    # if request.method == 'POST':
    #     form = VForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit = False)
    #         form.save()
    #         messages.success(request, 'Success')
    #         return redirect('volunteer_page')
    #     else:
    #          messages.error(request, "Sorry try again")
    # else:
    #     form = VForm()
    context = {
        'gallery': gallery,
        'banner': banner,

        # 'form':'form',



    }
    return render(request, 'SanskarSamaj/gallery.html', context)

def gallery_detail(request, slug):
    gallerys = Gallery.objects.filter(active = True).order_by('-date')
    # volunteer = Volunteer.objects.all().order_by('-date')
    gallery = Gallery.objects.get(slug=slug)
    banner = Banner.objects.all()

    more_images = MoreImage.objects.filter(active=True,image_title_id=gallery)

    # if request.method == 'POST':
    #     form = VForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit = False)
    #         form.save()
    #         messages.success(request, 'Success')
    #         return redirect('volunteer_page')
    #     else:
    #          messages.error(request, "Sorry try again")
    # else:
    #     form = VForm()

    context = {
        'gallery': gallery,
        'gallerys': gallerys,
        'more_images':more_images,
        'banner': banner,
        # 'volunteer': volunteer,

        # 'form': form

    }
    return render(request, 'SanskarSamaj/gallery_detail.html', context)

def causes_page(request):
    cause = Causes.objects.all().order_by('date')
    banner = Banner.objects.all()
    # volunteer = Volunteer.objects.all().order_by('date')


    page = request.GET.get('page', 1)
    paginator = Paginator(cause, 6)
    try:
        cause = paginator.page(page)
    except PageNotAnInteger:
        cause = paginator.page(1)
    except EmptyPage:
        cause = paginator.page(paginator.num_pages)

    # if request.method == 'POST':
    #     form = VForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit = False)
    #         form.save()
    #         messages.success(request, 'Success')
    #         return redirect('volunteer_page')
    #     else:
    #          messages.error(request, "Sorry try again")
    # else:
    #     form = VForm()


    context = {
        'cause': cause,

        'banner': banner,
        # 'form': form


    }
    return render(request, 'SanskarSamaj/causes.html', context)

def causes_detail(request, slug):
    cause = Causes.objects.get(slug=slug)
    causes = Causes.objects.all()
    banner = Banner.objects.all()
    # volunteer = Volunteer.objects.all().order_by('date')

    # if request.method == 'POST':
    #     form = VForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit = False)
    #         form.save()
    #         messages.success(request, 'Success')
    #         return redirect('volunteer_page')
    #     else:
    #          messages.error(request, "Sorry try again")
    # else:
    #     form = VForm()
    context = {
        'cause': cause,
        # 'volunteer': volunteer,

        'banner': banner,
        # 'form': form
    }
    return render(request, 'SanskarSamaj/causes_detail.html', context)





def volunteer_page(request):
    # volunteer = Volunteer.objects.all()
    banner = Banner.objects.all()

    # if request.method == 'POST':
    #     form = VForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit = False)
    #         form.save()
    #         messages.success(request, 'Success')
    #         return redirect('volunteer_page')
    #     else:
    #          messages.error(request, "Sorry try again")
    # else:
    #     form = VForm()
    context = {
        # 'volunteer': volunteer,
        # 'form':form,

        'banner': banner,
    }
    return render(request, 'SanskarSamaj/volunteer.html', context)

def contact_page(request):
    contact = ContactPage.objects.all()
    banner = Banner.objects.all()
    volunteer = Volunteer.objects.all().order_by('date')
    nav = Nav.objects.all()
    footer = Footer.objects.all()
    about = About.objects.all()
    latest_event2 = Events.objects.order_by('-pk')[0:2]
    if request.method == 'POST':
        form = CForm(request.POST)
        form2 = VForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = "{0} with email address {1} has sent you new message \n\n{2}".format(name, email, form.cleaned_data['message'])

            form.save(commit = False)
            try:
                send_mail(name, message, 'Sanskar Samaj <settings.EMAIL_HOST_USER>', ['sugatp454@gmail.com'])
            except:
                return HttpResponse('Invalid header found')
            form.save()
            messages.success(request, 'Success')
            return redirect('contact_page')
        elif form2.is_valid():
            form2.save(commit = False)
            form2.save()
            messages.success(request, 'Success')
            return redirect('volunteer_page')

        else:
            # return HttpResponse(form.errors)
            messages.error(request, "Sorry try again")
    else:
        form = CForm()
        form2 = VForm()



    context = {
        'contact': contact,
        'volunteer': volunteer,
        'form':form,
        'form2':form2,
        'footer':footer,
        'about':about,
        'nav': nav,
        'latest_event2': latest_event2,
        'banner': banner,
    }
    return render(request, 'SanskarSamaj/contact.html', context)

def about_page(request):
    about = About.objects.all().order_by('date')
    banner = Banner.objects.all()
    # volunteer = Volunteer.objects.all().order_by('date')
    testimonial = Testimonial.objects.order_by('-pk')[0:2]
    nav = Nav.objects.all()
    footer = Footer.objects.all()

    latest_event2 = Events.objects.order_by('-pk')[0:2]
    # if request.method == 'POST':
    #     form = VForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit = False)
    #         form.save()
    #         messages.success(request, 'Success')
    #         return redirect('volunteer_page')
    #     else:
    #          messages.error(request, "Sorry try again")
    # else:
    #     form = VForm()
    context = {
        'about': about,
        # 'volunteer': volunteer,
        'testimonial': testimonial,
        'footer':footer,
        'banner': banner,
        'nav': nav,
        'latest_event2': latest_event2,
        # 'form': form
    }


    return render(request, 'SanskarSamaj/about.html', context)

    # return render_to_response('SanskarSamaj/about.html', context, context_instance=RequestContext(request))


def events_page(request):
    event = Events.objects.all().order_by('-date')
    banner = Banner.objects.all()
    # volunteer = Volunteer.objects.all().order_by('date')
    nav = Nav.objects.all()
    footer = Footer.objects.all()
    about = About.objects.all()
    latest_event2 = Events.objects.order_by('-pk')[0:2]
    page = request.GET.get('page', 1)
    paginator = Paginator(event, 6)
    try:
        event = paginator.page(page)
    except PageNotAnInteger:
        event = paginator.page(1)
    except EmptyPage:
        event = paginator.page(paginator.num_pages)

    # if request.method == 'POST':
    #     form = VForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit = False)
    #         form.save()
    #         messages.success(request, 'Success')
    #         return redirect('volunteer_page')
    #     else:
    #          messages.error(request, "Sorry try again")
    # else:
    #     form = VForm()
    context = {
        'event': event,
        # 'volunteer': volunteer,
        'footer':footer,
        'about':about,
        'nav': nav,
        'latest_event2': latest_event2,
        'banner': banner,
        # 'form': form

    }
    return render(request, 'SanskarSamaj/events.html', context)

def events_detail(request, slug):
    event = Events.objects.get(slug=slug)
    banner = Banner.objects.all()
    events= Events.objects.all()
    # volunteer = Volunteer.objects.all().order_by('date')
    nav = Nav.objects.all()
    footer = Footer.objects.all()
    about = About.objects.all()
    latest_event2 = Events.objects.order_by('-pk')[0:2]
    # if request.method == 'POST':
    #     form = VForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit = False)
    #         form.save()
    #         messages.success(request, 'Success')
    #         return redirect('volunteer_page')
    #     else:
    #          messages.error(request, "Sorry try again")
    # else:
    #     form = VForm()
    context = {
        'event': event,
        'events': events,
        # 'volunteer': volunteer,
        'footer':footer,
        'about':about,
        'nav': nav,
        'latest_event2': latest_event2,
        'banner': banner,
        # 'form': form,
    }
    return render(request, 'SanskarSamaj/events_detail.html', context)


# def handler404(request):
#     return render(request, 'SanskarSamaj/404.html', status = 404)

# def handler500(request):
#     return render(request, 'SanskarSamaj/500.html', status = 500)






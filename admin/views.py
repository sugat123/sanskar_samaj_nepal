from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from admin.forms import *
from welfare import settings



def register(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    if request.method == "POST":
        form = AddUserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'user created with username {}'.format(user.username))
            return redirect('admin:register')
    else:
        form = AddUserForm()
    return render(request, 'admin/add_user.html', {'form': form})



def view_admin_user(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    
    users = User.objects.filter(is_superuser=True).order_by('-date_joined')

    return render(request, 'admin/admin_users.html', {'users': users, 'title': 'All Users'})

def view_staff_user(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')

    users = User.objects.exclude(is_superuser=True).order_by('-date_joined')

    return render(request, 'admin/staff_users.html', {'users': users, 'title': 'All Users'})





def update_admin_user(request, id):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = EditUserForm(request.POST or None, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, '{} updated'.format(user.username))
            return redirect('admin:view_admin_user')

    return render(request,'admin/edit_admin_user.html',{'user':user})

def update_staff_user(request, id):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')

    user = get_object_or_404(User,id=id)
    if request.method == 'POST':
        form = EditUserForm(request.POST or None, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, '{} updated'.format(user.username))
            return redirect('admin:view_staff_user')

    return render(request,'admin/edit_user.html',{'user':user})

def users_change_password(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('admin:dashboard')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'admin/change_password.html', {
        'form': form
    })


def deleteusers(request, id):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, '{} deleted'.format(user.username))
    return redirect('admin:our_users')

def index(request):
    
    sections = SectionComponent.objects.all()
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(request, username=username, password=password)
            if user and user.is_superuser:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                redirect_url = request.GET.get('next', 'admin:dashboard')
                messages.info(request, 'You are logged in as an admin .')
                return redirect(redirect_url)
            elif user and user.is_staff:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                redirect_url = request.GET.get('next', 'admin:dashboard')
                messages.info(request, 'You are logged in as a staff member.')
                return redirect(redirect_url)
            elif user and not user.is_active:
                messages.info(request, 'Your account is not active now.')
            else:
                messages.error(request, 'Invalid Username and Password')
        else:
            messages.error(request, 'Invalid Form')

    else:
        form = LoginForm()
    return render(request, 'admin/index.html', {'form': form,'title':'Admin Login', 'sections':sections})


def logout_user(request):

    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'logged out successfully')
        return redirect('/admin/')


def dashboard(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    events = Event.objects.all().order_by('-date')
    causes = Cause.objects.all().order_by('-date')
    return render(request, 'admin/dashboard.html', {'events':events,'causes':causes})


def view_setting(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    details = Detail.objects.all().order_by('-date')[0:1]
    settings = SectionComponent.objects.all().order_by('-date')[0:1]
    return render(request, 'admin/view_setting.html', {'settings': settings, 'details': details})


def edit_setting(request, id):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    banners = Banner.objects.all().order_by('-date')[0:1]
    return render(request, 'admin/view_banner.html', {'banners': banners})


def edit_banner(request, id):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    banner = get_object_or_404(Banner, id=id)
    if request.method == "POST":
        form = AddBannerForm(request.POST or None, request.FILES or None, instance=banner)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('admin:view_banner')
    return render(request, 'admin/edit_banner.html', {'banner': banner})


def view_event(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    events = Event.objects.all().order_by('-auto_date')
    return render(request, 'admin/view_event.html', {'events': events})


def add_event(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    event = get_object_or_404(Event, slug=slug)
    event.delete()
    messages.success(request, '{} Event deleted'.format(event.title))
    return redirect('admin:view_event')

def delete_selected_event(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    selected_events = Event.objects.filter(id__in=request.POST.getlist('events'))
    selected_events.delete()
    messages.success(request,'Deleted')
    return redirect('admin:view_event')

def delete_all_event(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    all_events = Event.objects.all()
    all_events.delete()
    messages.success(request, 'Deleted')
    return redirect('admin:view_event')


def detail_event(request, slug):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    event = get_object_or_404(Event, slug=slug)

    return render(request, 'admin/detail_event.html', {'event': event})



def view_cause(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    causes = Cause.objects.all().order_by('-date')
    return render(request, 'admin/view_cause.html', {'causes': causes})


def add_cause(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    cause = get_object_or_404(Cause, slug=slug)
    cause.delete()
    messages.success(request, '{} Cause deleted'.format(cause.title))
    return redirect('admin:view_cause')


def detail_cause(request, slug):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    cause = get_object_or_404(Cause, slug=slug)

    return render(request, 'admin/detail_cause.html', {'cause': cause})

def delete_selected_cause(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    selected_causes = Cause.objects.filter(id__in=request.POST.getlist('causes'))
    selected_causes.delete()
    messages.success(request,'Deleted')
    return redirect('admin:view_cause')

def delete_all_cause(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    all_causes = Cause.objects.all()
    all_causes.delete()
    messages.success(request, 'Deleted')
    return redirect('admin:view_cause')


def view_gallery(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    gallerys = Gallery.objects.all().order_by('-date')
    return render(request, 'admin/view_gallery.html', {'gallerys': gallerys})


def add_gallery(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    if request.method == 'POST':
        form = AddGalleryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery = form.save(commit=False)
            gallery.save()
            messages.success(request, ' Image added.')
            return redirect('admin:add_more_image')
    else:
        form = AddGalleryForm()
    return render(request, 'admin/add_gallery.html', {'form': form})

def add_more_image(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    gallery = Gallery.objects.all().order_by('-pk')
    if request.method == 'POST':
        form = MoreImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():

            more = form.save(commit=False)
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    img = MoreImage(image=formfile)
                    img.save()
            for g in gallery:
                more.image_title_id=g.id
            more.save()
            messages.success(request, ' Images added.')
            return redirect('admin:add_gallery')
        else:
            return HttpResponse(form.errors)
    else:
        form = MoreImageForm()
    return render(request, 'admin/more_image.html', {'form': form})


def edit_gallery(request, slug):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    gallery = get_object_or_404(Gallery, slug=slug)
    gallery.delete()
    messages.success(request, '{} image deleted'.format(gallery.image_title))
    return redirect('admin:view_gallery')

def delete_selected_gallery(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    selected_galleries = Gallery.objects.filter(id__in=request.POST.getlist('galleries'))
    selected_galleries.delete()
    messages.success(request,'Deleted')
    return redirect('admin:view_gallery')

def delete_all_gallery(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    all_galleries = Gallery.objects.all()
    all_galleries.delete()
    messages.success(request, 'Deleted')
    return redirect('admin:view_gallery')


def detail_gallery(request, slug):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    gallery = get_object_or_404(Gallery, slug=slug)

    return render(request, 'admin/detail_gallery.html', {'gallery': gallery})


def view_testimonial(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    testimonials = Testimonial.objects.all().order_by('-date')
    return render(request, 'admin/view_testimonial.html', {'testimonials': testimonials})


def add_testimonial(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
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
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    testimonial = get_object_or_404(Testimonial, slug=slug)
    testimonial.delete()
    messages.success(request, '{}  deleted'.format(testimonial.title))
    return redirect('admin:view_testimonial')

def delete_selected_testimonial(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    selected_testimonials = Testimonial.objects.filter(id__in=request.POST.getlist('testimonials'))
    selected_testimonials.delete()
    messages.success(request,'Deleted')
    return redirect('admin:view_testimonial')

def delete_all_testimonial(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    all_testimonials = Testimonial.objects.all()
    all_testimonials.delete()
    messages.success(request, 'Deleted')
    return redirect('admin:view_testimonial')


def detail_testimonial(request, slug):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    testimonial = get_object_or_404(Testimonial, slug=slug)

    return render(request, 'admin/detail_testimonial.html', {'testimonial': testimonial})


def contact_message(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    contacts = ContactForm.objects.all().order_by('-date')
    return render(request, 'admin/contact_message.html', {'contacts': contacts})


def volunteer_message(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    volunteers = VolunteerForm.objects.all().order_by('-date')
    return render(request, 'admin/volunteer_message.html', {'volunteers': volunteers})

def delete_message(request,id):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    message = get_object_or_404(ContactForm,id=id)
    message.delete()
    messages.success(request,'Deleted')
    return redirect('admin:contact_message')
def delete_volunteer(request,id):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    message = get_object_or_404(VolunteerForm, id=id)
    message.delete()
    messages.success(request, 'Deleted')
    return redirect('admin:volunteer_message')
def delete_selected_message(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    selected_messages = ContactForm.objects.filter(id__in=request.POST.getlist('messages'))
    selected_messages.delete()
    messages.success(request,'Deleted')
    return redirect('admin:contact_message')
def delete_selected_volunteer(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    selected_volunteer = VolunteerForm.objects.filter(id__in=request.POST.getlist('volunteers'))
    selected_volunteer.delete()
    messages.success(request, 'Deleted')
    return redirect('admin:volunteer_message')
def delete_all_message(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    all_messages = ContactForm.objects.all()
    all_messages.delete()
    messages.success(request, 'Deleted')
    return redirect('admin:contact_message')
def delete_all_volunteer(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Permission Denied.You have no permission to register users.')
        return redirect('admin:index')
    all_volunteer = VolunteerForm.objects.all()
    all_volunteer.delete()
    messages.success(request, 'Deleted')
    return redirect('admin:volunteer_message')



def send_mail_contact(request,id):
    contact = get_object_or_404(ContactForm,id=id)
    form = SendMailContact(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        send_mail(subject,message, 'Sanskar Samaj <settings.EMAIL_HOST_USER>', [contact])

        messages.success(request, 'Success')
        return redirect('admin:contact_message')

def send_mail_selected_contact(request):
    selected_contact = ContactForm.objects.filter(id__in=request.POST.getlist('messages'))
    form = SendMailContact(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        for contact in selected_contact:
            send_mail(subject,message, 'Sanskar Samaj <settings.EMAIL_HOST_USER>', [contact.email])
        messages.success(request, 'Success')
        return redirect('admin:contact_message')

def send_mail_all_contact(request):
    contacts = ContactForm.objects.all()
    form = SendMailContact(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        for contact in contacts:
            send_mail(subject,message, 'Sanskar Samaj <settings.EMAIL_HOST_USER>', [contact.email])
        messages.success(request, 'Success')
        return redirect('admin:contact_message')

def send_mail_volunteer(request,id):
    volunteer = get_object_or_404(VolunteerForm,id=id)
    form = SendMailVolunteer(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        send_mail(name,subject,message, 'Sanskar Samaj <settings.EMAIL_HOST_USER>', [volunteer])

        messages.success(request, 'Success')
        return redirect('admin:volunteer_message')

def send_mail_selected_volunteer(request):
    volunteer = VolunteerForm.objects.filter(id__in = request.POST.getlist('volunteers'))
    form = SendMailVolunteer(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        form.save(commit=False)
        send_mail(name,subject,message, 'Sanskar Samaj <settings.EMAIL_HOST_USER>', [volunteer])

        messages.success(request, 'Success')
        return redirect('admin:volunteer_message')
def send_mail_all_volunteer(request):
    volunteer = VolunteerForm.objects.all()
    form = SendMailVolunteer(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        send_mail(name,subject,message, 'Sanskar Samaj <settings.EMAIL_HOST_USER>', [volunteer])
        messages.success(request, 'Success')
        return redirect('admin:volunteer_message')


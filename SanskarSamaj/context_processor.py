from SanskarSamaj.models import *
from django.shortcuts import render, redirect
from SanskarSamaj.forms import VForm
from django.core.mail import send_mail
from django.contrib import messages

from admin.models import SectionComponent, Detail


def volunteer_page2(request):
    sections = SectionComponent.objects.all().order_by('-date')[0:1]
    details = Detail.objects.all().order_by('-date')[0:1]

    if request.method == 'POST':
        form = VForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = "{0} with email address {1} has sent you new message \n\n{2}".format(name, email,
                                                                                           form.cleaned_data['message'])
            form.save(commit=False)

            send_mail(name, message, 'Sanskar Samaj <settings.EMAIL_HOST_USER>', ['sugatp454@gmail.com'])

            form.save()
            messages.success(request, 'Success')
            # return redirect('volunteer_page')
        else:
            messages.error(request, "Sorry try again")
    else:
        form = VForm()

    return {'sections': sections, 'details': details, 'form': form}

import datetime

from django.db import models
from autoslug import AutoSlugField


class SectionComponent(models.Model):
    logo = models.ImageField(upload_to='setting', default='default.png')
    volunteer_image = models.ImageField(upload_to='setting', default='default.png')
    volunteer_bg_image = models.ImageField(upload_to='setting', default='default.png')
    volunteer_text = models.TextField(blank=True, null=True)
    about_title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    about_image = models.ImageField(upload_to='about', default='default.png')
    about_description = models.TextField()
    login_bg = models.ImageField(upload_to='setting', default='default.png')


class Detail(models.Model):
    facebook_link = models.URLField(default='https://www.facebook.com')
    twitter_link = models.URLField(default='https://www.twitter.com')
    insta_link = models.URLField(default='https://www.instagram.com')
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(default='https://www.yoursite.com')
    map_link = models.URLField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


class Banner(models.Model):
    index_banner = models.ImageField(upload_to='banner', default='default.png')
    causes_banner = models.ImageField(upload_to='banner', default='default.png')
    gallery_banner = models.ImageField(upload_to='banner', default='default.png')
    events_banner = models.ImageField(upload_to='banner', default='default.png')
    volunteer_banner = models.ImageField(upload_to='banner', default='default.png')
    about_banner = models.ImageField(upload_to='banner', default='default.png')
    contact_banner = models.ImageField(upload_to='banner', default='default.png')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Cause(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = AutoSlugField(unique_with='id', populate_from='title')
    description = models.TextField(blank=True, null=True)
    cause_image = models.ImageField(upload_to='cause', default='default.png')
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    views = models.IntegerField(default=0, blank=True, null=True)
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=60, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='testimonial', default='default.png', blank=True, null=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(unique_with='id', populate_from='title')

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image_title = models.CharField(max_length=100, blank=True, null=True)
    image_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery', default='default.png')
    date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(unique_with='id', populate_from='image_title')
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)


class MoreImage(models.Model):
    image_title = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='moreimage', default='default.png')
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)


class Event(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(unique_with='id', populate_from='title')
    date = models.DateField(default=datetime.datetime.today)
    time = models.TimeField( blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='events', default='default.png')
    venue = models.CharField(max_length=60, blank=True, null=True)
    views = models.IntegerField(default=0, blank=True, null=True)
    auto_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)


class VolunteerForm(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class ContactForm(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=60)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

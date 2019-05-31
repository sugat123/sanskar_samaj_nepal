from django.db import models
from autoslug import AutoSlugField
from django.utils.html import format_html


class Nav(models.Model):
    logo = models.ImageField(upload_to='nav', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def image_tag(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.logo.url))
    image_tag.short_description = "Logo"
    class Meta:
        verbose_name_plural = 'Logo'


class Banner(models.Model):
    index_banner = models.ImageField(upload_to='banner', default = 'default.png')
    causes_banner = models.ImageField(upload_to='banner', default = 'default.png')
    gallery_banner = models.ImageField(upload_to='banner', default = 'default.png')
    events_banner = models.ImageField(upload_to='banner', default = 'default.png')
    volunteer_banner = models.ImageField(upload_to='banner', default = 'default.png')
    about_banner = models.ImageField(upload_to='banner', default = 'default.png')
    contact_banner = models.ImageField(upload_to='banner', default = 'default.png')
    date = models.DateTimeField(auto_now_add=True)
    def event_banner(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.events_banner.url))

    def indexs_banner(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.index_banner.url))

    def cause_banner(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.causes_banner.url))

    def gallerys_banner(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.gallery_banner.url))

    def volunteers_banner(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.volunteer_banner.url))

    def abouts_banner(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.about_banner.url))

    def contacts_banner(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.contact_banner.url))
class Causes(models.Model):
    
    title = models.CharField(max_length=100)
    slug = AutoSlugField(unique_with='id', populate_from='title')
    description = models.TextField()
    cause_image = models.ImageField(upload_to='cause',  default = 'default.png')
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Cause'

    def image_tag(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.cause_image.url))


class Testimonial(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=60)
    review = models.TextField()
    image = models.ImageField(upload_to='testimonial', default = 'default.png')
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.image.url))


class Gallery(models.Model):
   
    image_title = models.CharField(max_length=100)
    image_date = models.DateField()
    image = models.ImageField(upload_to='gallery', default = 'default.png')
    date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(unique_with='id', populate_from='image_title')
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default = False)

    def image_tag(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.image.url))


class MoreImage(models.Model):
    image_title = models.ForeignKey(Gallery, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='moreimage', default = 'default.png')
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default = False)

    def image_tag(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.image.url))


    


class Events(models.Model):
    
    title = models.CharField(max_length=100)
    slug = AutoSlugField(unique_with='id', populate_from='title')
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='events', default = 'default.png')
    venue = models.CharField(max_length=60)
    auto_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default = False)

    def image_tag(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.image.url))

    # def date_only(self):
    #     return self.date.strftime('%B %d %Y')

    # def time_only(self):
    #     return self.date.strftime("%I:%M:%S %p")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Event'


class Volunteer(models.Model):
    image = models.ImageField(upload_to='volunteer', default = 'default.png')
    bg_image = models.ImageField(upload_to='volunteer', default = 'default.png')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

    def image_tag(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.image.url))

    def bg_image_tag(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.bg_image.url))

    class Meta:
        verbose_name_plural = 'Volunteer_Section'


class About(models.Model):
    
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='about', default = 'default.png')
    description = models.TextField()

    def image_tag(self):
        return format_html('<img href = "{0}" src="{0}" width = "100" height ="100" style = "object-fit: cover; border-radius: 50%;" />'.format(self.image.url))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'About_Section'


class Footer(models.Model):
    
    facebook_link = models.URLField(default='https://www.facebook.com')
    twitter_link = models.URLField(default='https://www.twitter.com')
    insta_link = models.URLField(default='https://www.instagram.com')
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Footer_Section'


class ContactPage(models.Model):
    
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    map_link = models.URLField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Contact_Section'


class VolunteerForm(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Message from Volunteers Form'


class ContactForm(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=60)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Message from Contacts Form'


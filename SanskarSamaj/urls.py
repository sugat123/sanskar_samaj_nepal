from django.urls import path
from SanskarSamaj import views
 
urlpatterns = [
    
    path('', views.index, name='index'),
    path('about/', views.about_page, name='about_page'),
    path('events/', views.events_page, name='events_page'),
    path('gallery/', views.gallery, name='gallery'),
    path('causes/', views.causes_page, name='causes_page'),
    path('gallery/<slug>/', views.gallery_detail, name='gallery_detail'),
    path('volunteer/', views.volunteer_page, name='volunteer_page'),
    path('contact/', views.contact_page, name='contact_page'),
     path('causes/<slug>/', views.causes_detail, name='causes_detail'),
     path('events/<slug>/', views.events_detail, name='events_detail'),
]
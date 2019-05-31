from django.urls import path

from admin import views

app_name = 'admin'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),

    path('view/event', views.view_event, name='view_event'),
    path('view/cause', views.view_cause, name='view_cause'),
    path('view/gallery', views.view_gallery, name='view_gallery'),
    path('view/testimonial', views.view_testimonial, name='view_testimonial'),
    path('contact/message', views.contact_message, name='contact_message'),
    path('volunteer/message', views.volunteer_message, name='volunteer_message'),
    path('view/banner', views.view_banner, name='view_banner'),
    path('add/banner/',views.add_banner,name='add_banner'),
    path('<int:id>/edit/banner', views.edit_banner, name='edit_banner'),
    path('add/setting/',views.add_setting,name='add_setting'),
    path('add/detail/',views.add_detail,name='add_detail'),
    path('<int:id>/edit/detail/',views.edit_detail,name='edit_detail'),

     path('<int:id>/edit/setting', views.edit_setting, name='edit_setting'),
    path('view/setting', views.view_setting, name='view_setting'),

    path('add/event', views.add_event, name='add_event'), 
     path('add/cause', views.add_cause, name='add_cause'),
     path('add/gallery', views.add_gallery, name='add_gallery'),
     path('add/testimonial', views.add_testimonial, name='add_testimonial'),
    # path('about/', views.about_page, name='about_page'),
    # path('events/', views.events_page, name='events_page'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('causes/', views.causes_page, name='causes_page'),
    # path('gallery/<slug>/', views.gallery_detail, name='gallery_detail'),
    # path('volunteer/', views.volunteer_page, name='volunteer_page'),
    # path('contact/', views.contact_page, name='contact_page'),
    #  path('causes/<slug>/', views.causes_detail, name='causes_detail'),
    #  path('events/<slug>/', views.events_detail, name='events_detail'),
]
from django.urls import path, reverse_lazy

from admin import views
from django.contrib.auth import views as auth_views

app_name = 'admin'

urlpatterns = [

    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('register/user/', views.register, name='register'),

    path('<int:id>/delete/user', views.deleteusers, name='delete_user'),
    path('change/password/', views.users_change_password, name='change_password'),




    path('view/admin/', views.view_admin_user, name='view_admin_user'),
    path('view/staff/', views.view_staff_user, name='view_staff_user'),
    path('<int:id>/update/admin/', views.update_admin_user, name='update_admin_user'),
    path('<int:id>/update/staff/', views.update_staff_user, name='update_staff_user'),
    path('view/event', views.view_event, name='view_event'),
    path('view/cause', views.view_cause, name='view_cause'),
    path('view/gallery', views.view_gallery, name='view_gallery'),
    path('view/testimonial', views.view_testimonial, name='view_testimonial'),
    path('contact/message', views.contact_message, name='contact_message'),
    path('volunteer/message', views.volunteer_message, name='volunteer_message'),
    path('view/banner', views.view_banner, name='view_banner'),
    path('add/banner/', views.add_banner, name='add_banner'),
    path('<int:id>/edit/banner', views.edit_banner, name='edit_banner'),
    path('add/setting/', views.add_setting, name='add_setting'),
    path('add/detail/', views.add_detail, name='add_detail'),
    path('<int:id>/edit/detail/', views.edit_detail, name='edit_detail'),

    path('<int:id>/edit/setting', views.edit_setting, name='edit_setting'),
    path('view/setting', views.view_setting, name='view_setting'),

    path('add/event', views.add_event, name='add_event'),
    path('add/cause', views.add_cause, name='add_cause'),
    path('add/gallery', views.add_gallery, name='add_gallery'),
    path('add/testimonial', views.add_testimonial, name='add_testimonial'),
    path('<slug>/delete/event/', views.delete_event, name='delete_event'),
    path('<slug>/delete/cause/', views.delete_cause, name='delete_cause'),
    path('<slug>/delete/image/', views.delete_gallery, name='delete_gallery'),
    path('<slug>/delete/testimonial/', views.delete_testimonial, name='delete_testimonial'),
    path('<slug>/detail/event/', views.detail_event, name='detail_event'),
    path('<slug>/detail/cause/', views.detail_cause, name='detail_cause'),
    path('<slug>/detail/gallery/', views.detail_gallery, name='detail_gallery'),
    path('<slug>/detail/testimonial/', views.detail_testimonial, name='detail_testimonial'),
    path('<slug>/edit/event/', views.edit_event, name='edit_event'),
    path('<slug>/edit/cause/', views.edit_cause, name='edit_cause'),
    path('<slug>/edit/gallery/', views.edit_gallery, name='edit_gallery'),
    path('<slug>/edit/testimonial/', views.edit_testimonial, name='edit_testimonial'),
    path('<int:id>/delete/message/', views.delete_message, name='delete_message'),
    path('<int:id>/delete/volunteer/', views.delete_volunteer, name='delete_volunteer'),
    path('delete/selected/volunteer/', views.delete_selected_volunteer, name='delete_selected_volunteer'),
    path('delete/all/message/', views.delete_all_message, name='delete_all_message'),
    path('<int:id>/contact/detail/', views.contact_detail, name='contact_detail'),
    path('<int:id>/volunteer/detail/', views.volunteer_detail, name='volunteer_detail'),
    path('delete/all/volunteer/', views.delete_all_volunteer, name='delete_all_volunteer'),
    path('<int:id>/send/mail/contact/', views.send_mail_contact, name='send_mail_contact'),
    path('<int:id>/send/mail/volunteer/', views.send_mail_volunteer, name='send_mail_volunteer'),
    path('all/send/mail/contact', views.send_mail_all_contact, name='send_mail_all_contact'),
    path('all/send/mail/volunteer/', views.send_mail_all_volunteer, name='send_mail_all_volunteer'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='admin/password_reset.html',
                                              email_template_name='admin/password_reset_email.html',
                                              success_url=reverse_lazy('admin:password_reset_done', ),
                                              from_email="Sanskar Samaj<yourmailuser01@gmail.com>",
                                              ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='admin/password_reset_done.html', ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='admin/password_reset_confirm.html',
                                                     success_url=reverse_lazy('admin:password_reset_complete', ),

                                                     ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='admin/password_reset_complete.html',

                                                      ), name='password_reset_complete')

]

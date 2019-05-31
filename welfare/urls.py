"""welfare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include
from welfare import settings
from django.contrib.auth import views as auth_views
from SanskarSamaj import views
from django.views.static import serve

# handler404 = views.handler404
# handler500 = views.handler500
urlpatterns = [
    
    path('admin/', include('admin.urls')),
    path('', include('SanskarSamaj.urls')),
    path('admin/password_reset/',auth_views.PasswordResetView.as_view(from_email="SanskarSamaj <anusha.rai1234@gmail.com>"),name='admin_password_reset'),
path(
    'admin/password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(),
    name='password_reset_done'),
path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm'),
path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name ='SanskarSamaj/password_reset_complete.html'),
    name='password_reset_complete'),



]+ static(settings.MEDIA_URL,serve, document_root= settings.MEDIA_ROOT)





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

from SanskarSamaj import views
from django.views.static import serve

handler404 = views.view404
handler500 = views.view500
handler403 = views.view403
handler400 = views.view400
handler405 = views.view405
urlpatterns = [
    
    path('admin/', include('admin.urls')),
    path('', include('SanskarSamaj.urls')),

]+ static(settings.MEDIA_URL,serve, document_root= settings.MEDIA_ROOT)





"""sih_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    #index page
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('admin_login_verified/<str:member>',views.admin_login_verified,name='admin_login_verified'),
    path('blog_page/',views.blog_page,name='blog_page'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('contact_send_mail',views.contact_send_mail,name='contact_send_mail'),

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
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
    path('get_training/<str:training>/index',views.index_from_getintouch,name='index'),
    path('get_training/<str:training>/blog',views.blog_from_getintouch,name='blog'),
    path('get_training/<str:training>/contact_us',views.contact_from_getintouch,name='contact'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('blog',views.blog_page,name='blog'),
    path('admin_login_verified/add_new_training',views.add_new_training,name='admin_login_verified'),
    path('delete_training',views.delete_training,name='delete_training'),
    path('admin_login_verified/<str:member>',views.admin_login_verified,name='admin_login_verified'),
    path('get_training/<str:training>/',views.get_training,name='get_training'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('contact_send_mail',views.contact_send_mail,name='contact_send_mail'),
    path('get_training/<str:training>/get_training_send_mail',views.get_training_send_mail,name='get_training_send_mail'),
    path('certificates',views.certificates,name='certificates'),
    path('transcripts',views.transcripts,name='transcripts'),
    path('badges',views.badges,name='badges'),
    path('admin_login_force',views.admin_login_force,name="admin_login_force")

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
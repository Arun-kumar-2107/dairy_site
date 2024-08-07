"""
URL configuration for e_comm_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from home.views import *
from 

urlpatterns = [
    path('',start,name='start'),

    path('home/',Home,name='home'),

    path('account/',account,name='account'),

    path('product/',product,name='product'),

    path('login/',log_in,name='login'),

    path('logout/',log_out,name='logout'),

    path ('register/',register,name='register'),
    
    path('admin/', admin.site.urls),
]

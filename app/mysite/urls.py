"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from webapp.views import welcome, product, contact, register, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('product', product, name='product'),
    path('contact', contact, name='contact'),

    #path('accounts', include('django.contrib.auth.urls')), #Gère automatiquement l'inscription
    #path('accounts/register/', register, name='register'), #CAREFUL, register isnt in the default django package
    #path('accounts/profile/', profile, name='profile')
]
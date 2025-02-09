"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('donor-dashboard/', views.donor_dashboard, name='donor_dashboard'),
    path('donation_add/', views.donation_add, name='donation_add'),

    path('request-food/', views.request_food, name='request_food'),
    path('request_add/', views.request_add, name='request_add'),

    path('logistics/', views.logistics, name='logistics'),
    path('navigate/<int:req_id>/<int:don_id>/', views.navigate, name='navigate'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('network/', views.network, name='network'),
    path('deliver_happiness/', views.deliver_happiness, name='deliver_happiness'),
    path('partner_ngo/', views.partner_ngo, name='partner_ngo'),
]

"""reportlogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('countries/', views.CountryList.as_view()),
    path('divisions/', views.DivisionList.as_view()),
    path('districts/', views.DistrictList.as_view()),
    path('sub-districts/', views.SubDistrictList.as_view()),
    path('assignment-list/', views.AssignmentList.as_view()),
    path('create-data-form/', views.DataCollectForm.as_view()),
    path('data-list/', views.DataList.as_view()),
    path('data-details/<int:id>/', views.DataDetails.as_view()),
    path('service-list/', views.ServiceList.as_view()),
]

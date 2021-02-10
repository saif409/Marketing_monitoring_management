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
from.import views

urlpatterns = [
    path('', views.admin_home, name="admin_home"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('surveyor-list/<str:filter>/', views.surveyor_list, name="surveyor_list"),
    path('surveyor-details/<int:id>/', views.view_surveyor, name="view_surveyor"),
    path('update-surveyor/<int:id>/', views.update_surveyor, name="update_surveyor"),
    path('remove-surveyor/<int:id>/', views.remove_surveyor, name="remove_surveyor"),
    path('register-surveyor/', views.register_surveyor, name="register_surveyor"),
    path('country/', views.country, name="country"),
    path('update-country/<int:id>/', views.update_country, name="update_country"),
    path('country_remove/<int:id>/', views.country_remove, name="country_remove"),

    path('add_division/', views.add_division, name="add_division"),
    path('update-division/<int:id>/', views.update_division, name="update_division"),
    path('remove-division/<int:id>/', views.remove_division, name="remove_division"),
    path('add_district/', views.add_district, name="add_district"),
    path('update-district/<int:id>/', views.update_district, name="update_district"),
    path('remove_district/<int:id>/', views.remove_district, name="remove_distrcit"),
    path('add_sub_district/', views.add_sub_district, name="add_sub_district"),
    path('update-sub-district/<int:id>/', views.update_sub_district, name="update_sub_district"),
    path('remove-sub-district/<int:id>/', views.remove_subdistrict, name="remove_subdistrict"),


    path('notifications/', views.notifications, name="notifications"),
    path('collecting-data-list/', views.collecting_data_list, name="collecting_data_list"),
    path('data-collecting-form/', views.create_data_form, name="create_data_form"),
    path('collect-data-view/<int:id>/', views.collect_data_view, name="collect_data_view"),
    path('collect_data_delete/<int:id>/', views.collect_data_delete, name="collect_data_delete"),
    path('create-collect-form/', views.create_collect_form, name="create_collect_form"),
    path('view-form/<int:id>/', views.view_form, name="view_form"),
    path('form_delete/<int:id>/', views.form_delete, name="form_delete"),

]

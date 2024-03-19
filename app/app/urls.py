"""
URL configuration for app project.

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

from car.views import (index,
                       car_table, owner_detail,
                       add_car, edit_car, delete_car,
                       add_owner, edit_owner, delete_owner,
                       statistics)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cars/', car_table, name='cars'),
    path('add-car/', add_car, name='add_car'),
    path('edit-car/<int:car_id>', edit_car, name='edit_car'),
    path('delete-car/<int:car_id>', delete_car, name='delete_car'),

    path('owner/<int:owner_id>/', owner_detail, name='owner'),
    path('add-owner/', add_owner, name='add-owner'),
    path('edit-owner/<int:owner_id>/', edit_owner, name='edit-owner'),
    path('delete-owner/<int:owner_id>/', delete_owner, name='delete-owner'),

    path('statistics/', statistics, name='statistics')
]

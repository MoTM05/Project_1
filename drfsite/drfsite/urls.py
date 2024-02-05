"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path, include, re_path

from reports.views import *
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .yasg import urlpatterns as doc_urls

schema_view = get_swagger_view(title='Schema API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/authentification/', include('rest_framework.urls')),
    path('api/v1/equipmentlist/', EquipmentAPIList.as_view()),
    path('api/v1/equipmentlist_create/', EquipmentAPICreate.as_view()),
    path('api/v1/equipmentlist_update/<int:pk>/', EquipmentAPIUpdateDestroy.as_view()),
    path('api/v1/orderslist/', OrdersAPIList.as_view()),
    path('api/v1/orderslist_create/', OrdersAPICreate.as_view()),
    path('api/v1/orderslist_update/<int:pk>/', OrdersAPIUpdateDestroy.as_view()),
    path('api/v1/reportslist/', ReportsAPIList.as_view()),
    path('api/v1/report_create/', ReportsAPICreate.as_view()),
    path('api/v1/report_update/<int:pk>/', ReportsAPIUpdateDestroy.as_view()),
]

urlpatterns += doc_urls
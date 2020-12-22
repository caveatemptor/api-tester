"""apitest URL Configuration
"""
from django.contrib import admin
from django.urls import path
from core.views import home, endpoints

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('project/<slug:project>', endpoints)
]

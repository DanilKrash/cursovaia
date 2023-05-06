from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('service/', views.service, name='services'),
    path('contacts/', views.contact, name='contacts'),
]

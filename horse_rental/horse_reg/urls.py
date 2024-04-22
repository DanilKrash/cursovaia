from django.urls import path, include
from horse_reg.views import RegisterView

from horse_reg import views

app_name = 'custom_horse_reg'

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
]

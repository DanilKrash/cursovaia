from django.urls import path, include
from horse_reg.views import RegisterView


app_name = 'custom_horse_reg'

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
]

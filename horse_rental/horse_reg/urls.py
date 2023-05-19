from django.urls import path
from horse_reg.views import RegisterView

app_name = 'custom_horse_reg'

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='register'),
]

from django.urls import path, include
from horse_reg.views import RegisterView

from horse_reg import views

app_name = 'custom_horse_reg'

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('create_profile/<str:username>/', views.create_profile, name='create_profile'),
    path('update_profile/<str:username>/', views.update_profile, name='update_profile'),
    path('my_orders/<str:username>/', views.my_orders, name='my_orders'),
    path('my_orders/<int:ord_id>/delete/', views.delete_my_orders, name='delete_my_orders'),
]

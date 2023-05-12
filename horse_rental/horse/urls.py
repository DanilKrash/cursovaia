from django.urls import path
from horse import views
from horse.views import service_detail_view, service_list_view

app_name = 'horse'

urlpatterns = [
    path('', views.main, name='main'),
    path('services/', service_list_view, name='services'),
    path('<int:service_id>/', service_detail_view, name='detail'),
]

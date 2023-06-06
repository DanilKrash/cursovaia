from django.urls import path
from horse import views
from horse.views import service_detail_view, service_list_view, service_order_view

app_name = 'horse'

urlpatterns = [
    path('', views.main, name='main'),
    path('services/<int:page_num>/', service_list_view, name='services'),
    path('services/', service_list_view, name='first_service'),
    path('<int:service_id>/', service_detail_view, name='detail'),
    path('<int:order_id>/', service_order_view, name='order'),
]

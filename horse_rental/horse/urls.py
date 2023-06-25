from django.urls import path
from horse import views
from horse.views import service_detail_view, service_list_view, order_view, trainer_view, horse_view

app_name = 'horse'

urlpatterns = [
    path('', views.main, name='main'),
    path('services/<int:page_num>/', service_list_view, name='services'),
    path('services/', service_list_view, name='first_service'),
    path('detail/<int:service_id>/', service_detail_view, name='detail'),
    path('order/<int:order_id>/', order_view, name='order'),
    path('trainer/<int:trainer_id>/', trainer_view),
    path('horse/<int:horses_id>/', horse_view),
]

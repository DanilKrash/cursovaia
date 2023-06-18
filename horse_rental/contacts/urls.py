from django.urls import path
from contacts.views import contacts_view

app_name = 'contacts'

urlpatterns = [
    path('contacts/', contacts_view, name='contacts')
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('horse.urls', namespace='hor')),
    path('auth/', include('horse_reg.urls', namespace='reg')),
    path('', include('horse.urls', namespace='main')),
    path('accounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

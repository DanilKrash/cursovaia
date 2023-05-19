from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('horse.urls', namespace='hor')),
    path('', include('horse.urls', namespace='main')),
    path('auth/', include('horse_reg.urls', namespace='reg'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns_swagger as doc_urls

urlpatterns = [path('admin/', admin.site.urls),
               path('', include('cars.urls')),
               path('', include('users.urls')),
               ] + doc_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

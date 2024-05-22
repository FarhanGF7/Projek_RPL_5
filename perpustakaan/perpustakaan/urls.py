from django.contrib import admin

from django.urls import path, include

############### conf untuk menamilkan gambar yang sudah di upload pada folder media ###############
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('sistem_perpus.urls')),
]

############### untuk menampilkan gambar yang sudah di upload pada folder media ###############
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings.base import MEDIA_ROOT, MEDIA_URL

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
    path('', include('apps.main.urls')),
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

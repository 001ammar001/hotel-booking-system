from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path("", include("accounts.urls")),
    path("", include("hotel.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

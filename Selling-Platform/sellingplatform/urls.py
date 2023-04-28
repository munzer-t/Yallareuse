from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from custom_auth.views import home


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('custom_auth.urls')),
    path('product/', include('product.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
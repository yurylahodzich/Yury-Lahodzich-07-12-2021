from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('chat.urls')),
                  re_path(r'^media/(?P<path>.)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  re_path(r'^static/(?P<path>.)$', serve, {'document_root': settings.STATIC_ROOT}),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)

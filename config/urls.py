import imp
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/', include('review.urls')),
    path('account/', include('allauth.urls')),
    path('elbHealthCheck/', lambda request: HttpResponse('ok'), name="elb_healthcheck"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
#    + static(config.settings.STATIC_URL, document_root=config.settings.STATIC_ROOT)


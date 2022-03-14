from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/', include('review.urls')),
    path('account/', include('allauth.urls')),
    path('elbHealthCheck/', lambda request: HttpResponse('ok'), name="elb_healthcheck"),
]

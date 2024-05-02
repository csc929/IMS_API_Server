"""
Definition of urls for IMS_API_Server.
"""

from datetime import datetime
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, static
from django.urls import re_path
from rest_framework.authtoken import views as authviews
from app import views

admin.site.site_title = "IMS site admin"
admin.site.site_header = "IMS Dashboard"
admin.site.index_title = "Site Administration"

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    re_path(r'^api/api-token-auth/', authviews.obtain_auth_token),
    re_path(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/v2/accounts/', include('Accounts.urls', namespace='accounts')),
    re_path(r'^api/v2/', include('IMS_Control.urls', namespace='api')),
]

from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render


urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^tariff/', include('tariff.urls')),
    url(r'^contact/', include('contacts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^tmpl/(.*)$', render),
]

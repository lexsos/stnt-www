from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tmpl/(.*)$', render),
]

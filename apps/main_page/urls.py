from django.conf.urls import patterns, url
from publications.views import PublicationListView

from .models import Content


urlpatterns = [
    url(r'^$', PublicationListView.as_view(model=Content), name='main_page')
]


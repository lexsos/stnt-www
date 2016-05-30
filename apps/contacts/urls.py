from django.conf.urls import patterns, url
from publications.views import PublicationListView

from .models import Contact


urlpatterns = [
    url(r'^$', PublicationListView.as_view(model=Contact), name='contact_list'),
]

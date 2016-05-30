from django.conf.urls import url
from publications.views import PublicationListView

from .models import Tariff


urlpatterns = [
    url(r'^$', PublicationListView.as_view(model=Tariff), name='tariff_list'),
]

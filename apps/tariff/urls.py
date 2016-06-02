from django.conf.urls import url
from publications.views import PublicationListView
from django.views.generic import TemplateView

from .models import Tariff
from .views import AddConnectRequest


urlpatterns = [
    url(r'^$', PublicationListView.as_view(model=Tariff), name='tariff_list'),
    url(r'^add_connect_request/$', AddConnectRequest.as_view(), name='tariff_add_connect_request'),
    url(r'^success_connect_request/$', TemplateView.as_view(template_name="tariff/connect_request_success.html"), name='tariff_connect_request_success'),
]

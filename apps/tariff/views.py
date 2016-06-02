from django.views.generic import FormView
from django.core.urlresolvers import reverse

from .forms import ConnectRequestForm


class AddConnectRequest(FormView):

    form_class = ConnectRequestForm
    template_name = 'tariff/connect_request_form.html'

    def get_success_url(self):
        return reverse('tariff_connect_request_success')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return super(AddConnectRequest, self).form_valid(form)

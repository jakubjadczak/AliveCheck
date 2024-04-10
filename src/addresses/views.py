from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import IPAddress
from .forms import IPAddressForm
from django.contrib import messages
from .utils import calc_subnet


class IPAddressCreateView(CreateView):
    model = IPAddress
    form_class = IPAddressForm
    template_name = "addresses/create_address.html"
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        address = form.cleaned_data["address"]
        mask = form.cleaned_data["mask"]

        subnet = calc_subnet(address, mask)
        form.instance.subnet = subnet
        form.save()

        messages.success(self.request, "IP Address created successfully!")
        return super().form_valid(form)

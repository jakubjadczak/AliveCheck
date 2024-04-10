from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import IPAddress
from .forms import IPAddressForm, GroupForm, LabelForm, VlanForm
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


class GroupCreateView(CreateView):
    model = IPAddress
    form_class = GroupForm
    template_name = "addresses/create_group.html"
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        messages.success(self.request, "Group created successfully!")
        return super().form_valid(form)


class LabelCreateView(CreateView):
    model = IPAddress
    form_class = LabelForm
    template_name = "addresses/create_label.html"
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        messages.success(self.request, "Label created successfully!")
        return super().form_valid(form)


class VlanCreateView(CreateView):
    model = IPAddress
    form_class = VlanForm
    template_name = "addresses/create_vlan.html"
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        messages.success(self.request, "Vlan created successfully!")
        return super().form_valid(form)

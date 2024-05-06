from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views import View
from .models import IPAddress, Group, Vlan, Label, PingStat
from .forms import IPAddressForm, GroupForm, LabelForm, VlanForm
from django.contrib import messages
from django.utils import timezone
from .utils import (
    calc_subnet,
    simple_chart,
    ping_ip,
    PingParmas,
    PingResponse,
    response_time_chart,
)


class IPAddressCreateView(CreateView):
    model = IPAddress
    form_class = IPAddressForm
    template_name = "addresses/create_address.html"
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        address = form.cleaned_data["address"]
        mask = form.cleaned_data["mask"]
        subnet = form.cleaned_data["subnet"]
        print(mask, subnet)

        if mask != "" and subnet == "":
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


class IPAddressesListView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        filter_list = ["group", "subnet", "vlan"]
        obj = kwargs.get("obj", None)
        cond = kwargs.get("cond", None)

        if obj == "subnet":
            cond = cond.replace("-", "/")

        if obj in filter_list and cond is not None:
            addresses = IPAddress.objects.filter(**{obj: cond})
        else:
            addresses = IPAddress.objects.all()

        groups = Group.objects.all()
        vlans = Vlan.objects.all()
        labels = Label.objects.all()
        subnets = IPAddress.objects.get_subnets()

        print(subnets)

        context = {
            "addresses": addresses,
            "groups": groups,
            "vlans": vlans,
            "labels": labels,
            "subnets": subnets,
            "now": timezone.now(),
        }

        print(context)

        return render(request, "addresses/ip_addr_list_view.html", context)


class IPAddresessDetailView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        address_pk = kwargs.get("pk", None)
        address = IPAddress.objects.get(pk=address_pk)
        ping_stats = PingStat.objects.filter(address=address).order_by("-timestamp")

        items = response_time_chart(address)

        context = {
            "address": address,
            "ping_stats": ping_stats,
        }

        context = {**context, **items}

        return render(request, "addresses/address_details.html", context)


class ManuallyPingView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        print(pk)
        address = get_object_or_404(
            IPAddress, id=pk
        )  # TODO checking if address exists, duplicate
        result = ping_ip(address)
        response = PingResponse(**result)

        response_dict = response.model_dump()
        response_dict["address"] = address

        PingStat.objects.create(**response_dict)

        messages.success(request, "Ping result saved successfully!")

        return redirect(reverse("addrs:address_detail", kwargs={"pk": address.pk}))

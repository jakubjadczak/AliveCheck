from django.urls import path
from .views import IPAddressCreateView, GroupCreateView, LabelCreateView, VlanCreateView

app_name = "addrs"

urlpatterns = [
    path("addr/create/", IPAddressCreateView.as_view(), name="create"),
    path("group/create/", GroupCreateView.as_view(), name="group"),
    path("label/create/", LabelCreateView.as_view(), name="label"),
    path("vlan/create/", VlanCreateView.as_view(), name="vlan"),
]

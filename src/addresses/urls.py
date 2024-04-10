from django.urls import path
from .views import IPAddressCreateView

app_name = "addrs"

urlpatterns = [
    path("create/", IPAddressCreateView.as_view(), name="create"),
]

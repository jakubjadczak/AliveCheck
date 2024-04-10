from django.contrib import admin
from .models import Group, Label, Vlan, IPAddress, PingStat


class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


class LabelAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


class VlanAdmin(admin.ModelAdmin):
    list_display = ("number", "name", "description")
    search_fields = ("name", "number")


class IPAddressAdmin(admin.ModelAdmin):
    list_display = ("address", "mask", "group", "subnet", "description")
    list_filter = ("group", "vlan")
    search_fields = ("address",)
    filter_horizontal = ("label",)


class PingStatAdmin(admin.ModelAdmin):
    list_display = ("address", "timestamp", "avarage_response", "is_alive")
    list_filter = ("is_alive",)
    search_fields = ("address__address",)


admin.site.register(Group, GroupAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Vlan, VlanAdmin)
admin.site.register(IPAddress, IPAddressAdmin)
admin.site.register(PingStat, PingStatAdmin)

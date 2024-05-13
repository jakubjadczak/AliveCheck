from django import template
from ..models import PingStat

register = template.Library()


def change_slash(value):
    return value.replace("/", "-")


def get_last_ping(address):
    return PingStat.objects.get_last_ping(address).timestamp


def get_status(address):
    stat = PingStat.objects.get_last_ping(address)
    if stat.is_alive:
        return True
    return False


register.filter("change_slash", change_slash)
register.filter("get_last_ping", get_last_ping)
register.filter("get_status", get_status)

from django import template

register = template.Library()


def change_slash(value):
    return value.replace("/", "-")


register.filter("change_slash", change_slash)

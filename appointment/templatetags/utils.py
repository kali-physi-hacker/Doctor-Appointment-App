from django import template


register = template.Library()


@register.filter(name="empty_string")
def return_string(value):
    return ""

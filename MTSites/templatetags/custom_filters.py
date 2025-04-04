from django import template
register = template.Library()

@register.filter(name='defined')
def defined(value, arg):
    return value if value is not None else arg
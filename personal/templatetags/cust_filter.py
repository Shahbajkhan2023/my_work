from django import template
register = template.Library()


def first_two_upper(value):
    result = value[:2].upper()+value[2:]
    return result

register.filter('f2upper', first_two_upper)


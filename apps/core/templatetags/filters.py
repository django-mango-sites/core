import decimal
from django import template

register = template.Library()


@register.filter
def short_email(string):

    if string is None:
        return None

    if type(string) is not str:
        return string

    if '@' in string:
        string = string[string.index('@'):]

    return string


@register.filter
def currency(value):

    if value is None:
        return None

    if not isinstance(value, (int, float, decimal.Decimal)):
        return value

    value = "${:,.2f}".format(round(float(value), 2))

    return value
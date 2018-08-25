from django import template
from datetime import datetime

register = template.Library()


def print_timestamp(timestamp):
    try:
        ts = float(timestamp)
    except ValueError:
        return None
    return datetime.utcfromtimestamp(ts).strftime('%B %-d, %Y')


register.filter(print_timestamp)

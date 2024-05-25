from django import template
from reviews.models import Review, Ticket

register = template.Library()


@register.filter
def isinstanceof(value, class_name):
    if class_name == "Review":
        return isinstance(value, Review)
    elif class_name == "Ticket":
        return isinstance(value, Ticket)
    return False

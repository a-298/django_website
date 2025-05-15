from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter
def remove_images_only(value):
    return mark_safe(re.sub(r'<img\b[^>]*>', '', str(value)))
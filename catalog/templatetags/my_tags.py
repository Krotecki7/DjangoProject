from django import template

register = template.Library()


@register.filter()
def media_filter():
    if path:
        return f"media/{path}"
    return "#"

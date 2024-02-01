from django import template

register = template.Library()


@register.filter
def resize_img(height, width):
    window_width = 200
    window_height = 241
    if width > window_width:
        ratio = width // window_width
        height /= ratio
        width /= ratio
    else:
        ratio = window_width // width

    return [height, width]

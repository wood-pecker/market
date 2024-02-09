from django import template

register = template.Library()


@register.filter
def resize_img(width, height):
    max_width = 200
    max_height = 241
    ratio = min(max_width / width, max_height / height)

    return int(ratio * width), int(ratio * height)

from django import template

from shop.models import Category

register = template.Library()


@register.filter
def resize_img(width, height):
    max_width = 200
    max_height = 241
    ratio = min(max_width / width, max_height / height)

    return int(ratio * width), int(ratio * height)


@register.simple_tag
def get_category():
    return Category.objects.all()

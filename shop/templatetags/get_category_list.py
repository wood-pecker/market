from django import template
from shop.models import Category

register = template.Library()


@register.inclusion_tag('shop/templates/base.html')
def get_category():
    category_list = []
    for item in Category.objects.all():
        category_list.append(item.name)
    return {"category_list": category_list}

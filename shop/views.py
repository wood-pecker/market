from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Category, Product


class HomePage(ListView):
    model = Product
    
    
class SortByCategory(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    allow_empty = False
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # current_category = Category.objects.filter(pk=self.kwargs['id'])
        context["current_category"] = self.kwargs['id']
        print(context["current_category"])
        return context
    
    
    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['id'])
    

class ProductCard(DetailView):
    model = Product
    
    
class Login(TemplateView):
    template_name = 'shop/login.html'


class Register(TemplateView):
    template_name = 'shop/register.html'

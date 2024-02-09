from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product


class HomePage(ListView):
    model = Product
    

class ProductCard(DetailView):
    model = Product
    
    
class Login(TemplateView):
    template_name = 'shop/login.html'


class Register(TemplateView):
    template_name = 'shop/register.html'

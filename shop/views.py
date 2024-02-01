from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


class HomePage(ListView):
    model = Product
    

class ProductCard(DetailView):
    model = Product

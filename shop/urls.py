from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('product/<pk>/', ProductCard.as_view()),
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
]

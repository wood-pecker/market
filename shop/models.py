from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class Base(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created_at']
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
    phone = models.CharField()
    photo = models.ImageField(blank=True, upload_to='userphotos/%Y/%m/%d/')
    
    
class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-id']
        
    def __str__(self):
        return self.name
    
        
    name = models.CharField(db_index=True, verbose_name = 'Категория')
    

class Status(models.Model):
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['id']
        
    def __str__(self):
        return self.name
        
    name = models.CharField(db_index=True, verbose_name = 'Статус')
    
    
class ProductPhoto(Base):
    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'
        
    def __str__(self):
        return self.photo.name
    
        
    photo = models.ImageField(upload_to='product_photos/') 
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='product_photos'
    ) 
          
    
class Product(Base):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
    def __str__(self):
        return self.name
    
        
    name = models.CharField(max_length=80, verbose_name = 'Товар')
    description = models.TextField(max_length=500, verbose_name = 'Описание')
    price = models.FloatField(verbose_name = 'Цена')
    amount = models.IntegerField(verbose_name = 'Остаток на складе')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='product'
    )
    # photos = models.ManyToManyField(ProductPhoto, related_name='products')
    
    
class Order(Base):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
    
    products = models.ManyToManyField(Product, related_name='products')
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='order'
    )
    address = models.CharField(verbose_name = 'Адрес доставки')
    desired_delivery_date = models.DateTimeField(
        blank=True, null=True, verbose_name = 'Желаемое время доставки'
    )
    actual_delivery_date = models.DateTimeField(
        blank=True, null=True, verbose_name = 'Фактическое время доставки'
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, related_name='order'
    )
    
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, Order, Product, Category, Status, ProductPhoto


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("id", "first_name", "last_name")
    list_filter = ("id", "first_name", "last_name")     
    fields = (
        "username","first_name", "last_name", "email", "phone", "date_joined",
        "get_photo", "photo"
    )
    readonly_fields = ("get_photo", "date_joined")
    
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="120">')
        
    get_photo.short_description = "Фото пользователя"


class BaseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")
    list_filter = ("id", "name")
    
    
class ProductPhotoAdmin(admin.ModelAdmin):
    fields = ("photo", "get_photo", "product")
    readonly_fields = ("get_photo",)
    
    
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="120">')
        
    get_photo.short_description = "Фото пользователя"


admin.site.register(User, UserAdmin)
admin.site.register(Order)
admin.site.register(Product, BaseAdmin)
admin.site.register(Category, BaseAdmin)
admin.site.register(Status, BaseAdmin)
admin.site.register(ProductPhoto, ProductPhotoAdmin)

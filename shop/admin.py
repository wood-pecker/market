from django.contrib import admin

from .models import User, Order, Product, Category


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id", "first_name", "last_name", "email", "phone", "user_photo"
    )
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("id", "first_name", "last_name")
    list_filter = ("id", "first_name", "last_name")
    

admin.site.register(User, UserAdmin)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category)



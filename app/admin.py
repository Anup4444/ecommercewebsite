from sre_constants import BRANCH
from django.contrib import admin
from .models import Category, Sub_Category, Product, Contact_us, Order, Brand
# Register your models here.
admin.site.register(Category)
admin.site.register(Sub_Category)

admin.site.register(Product)
# admin.site.register(Contact_us)
admin.site.register(Order)
# brand
admin.site.register(Brand)


@admin.register(Contact_us)
class contactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message']

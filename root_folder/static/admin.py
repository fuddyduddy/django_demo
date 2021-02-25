from django.contrib import admin

from .models import (Employee, Customer, Vendor, Product, Order)#, TestModel)

# Register your models here.
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Product)

class OrderForm(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderForm)

#admin.site.register(TestModel)
from django.db import models

from django.urls import reverse

from django.core.validators import MinValueValidator
from decimal import Decimal

# all_books = Book.objects.all()
# wild_books = Book.objects.filter(title__contains='wild')
# number_wild_books = wild_books.count()

class Employee(models.Model):
    lastName        = models.CharField(max_length=60)
    firstName       = models.CharField(max_length=50)
    department      = models.CharField(max_length=100)
    age             = models.PositiveSmallIntegerField(default=0, help_text='Age: 0-99')
    position        = models.CharField(max_length=100)
    department      = models.CharField(max_length=100)
    email           = models.EmailField(help_text='Input email address here (max length = 254).')

    class Meta:
        ordering = ['lastName', 'firstName']

    def __str__(self):
        return f'{self.lastName} {self.firstName}'

    # def get_absolute_url(self):
    #     pass
    #     return reverse('model-detail-view', args=[str(self.id)])

class Customer(models.Model):
    name            = models.CharField(max_length=100)
    address         = models.CharField(max_length=300)
    contactPerson   = models.CharField(max_length=50)
    email           = models.EmailField(help_text='Input email address here (max length = 254).')
    telNumber       = models.DecimalField(max_digits=8, decimal_places=0, help_text='local numbers only (8-digit)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])

class Vendor(models.Model):
    name            = models.CharField(max_length=100)
    address         = models.CharField(max_length=300)
    contactPerson   = models.CharField(max_length=50)
    email           = models.EmailField(help_text='Input email address here (max length = 254).')
    telNumber       = models.DecimalField(max_digits=8, decimal_places=0, help_text='local numbers only (8-digit)')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     pass
    #     return reverse('model-detail-view', args=[str(self.id)])

class Product(models.Model):
    #id     = models.CharField()
    auto_id         = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=100)
    description     = models.CharField(max_length=100)
    unit            = models.DecimalField(max_digits=8, decimal_places=0)
    unitCost        = models.DecimalField(max_digits=8, decimal_places=0)
    unitSalesprice  = models.DecimalField(max_digits=8, decimal_places=0, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.auto_id)])

class Order(models.Model):
    orderID         = models.AutoField(primary_key=True)
    customer        = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    product         = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    #markUp          = models.StringField(validators=[valid_pct])
    orderDate       = models.DateField(null=True, blank=True) # In real case, can't be null / blank.
    unit_sold       = models.DecimalField(max_digits=9, decimal_places=0, help_text="max_digits = 9", validators=[MinValueValidator(int('1'))], null=True)
    costs           = models.CharField(max_length=100, null=True)

    # product2         = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    # unit_sold2       = models.DecimalField(max_digits=9, decimal_places=0, help_text="max_digits = 9", validators=[MinValueValidator(int('1'))], null=True)
    # costs2           = models.CharField(max_length=100, null=True)
    # product3         = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    # unit_sold3       = models.DecimalField(max_digits=9, decimal_places=0, help_text="max_digits = 9", validators=[MinValueValidator(int('1'))], null=True)
    # costs3           = models.CharField(max_length=100, null=True)
    # product4         = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    # unit_sold4       = models.DecimalField(max_digits=9, decimal_places=0, help_text="max_digits = 9", validators=[MinValueValidator(int('1'))], null=True)
    # costs4           = models.CharField(max_length=100, null=True)
    # product5         = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    # unit_sold5       = models.DecimalField(max_digits=9, decimal_places=0, help_text="max_digits = 9", validators=[MinValueValidator(int('1'))], null=True)
    # costs5           = models.CharField(max_length=100, null=True)

    # def valid_pct(value):
    #     if value.endswith("%"):
    #         return 1 + float(value[:-1])/100
    #     else:
    #         try:
    #             return float(value)
    #         except ValueError:          
    #             raise ValidationError(
    #                 _('%(value)s is not a valid pct'),
    #                     params={'value': value},
    #             )
    
    def __str__(self):
        return self.orderID

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.orderID)])

# class TestModel(models.Model):
#     name            = models.CharField(max_length=100)
#     summary         = models.CharField(max_length=300, null=True)
#     customer        = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
#     product         = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
#     unit_sold       = models.DecimalField(max_digits=9, decimal_places=0, help_text="max_digits = 9", validators=[MinValueValidator(int('1'))], null=True)
#     costs           = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.name


from django import forms
from .models import Order, Customer, Product #, TestModel

# Better Form Name can be used as <label> when rendering in templates, (capitalize 1st Char, and _ as space...etc)

class CustomerForm(forms.ModelForm):
    name            = forms.CharField(max_length=100)
    address         = forms.CharField(max_length=300)
    contactPerson   = forms.CharField(max_length=50)
    email           = forms.EmailField(help_text='Input email address here (max length = 254).')
    telNumber       = forms.DecimalField(max_digits=8, decimal_places=0, help_text='local numbers only (8-digit)')

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        pass

    class Meta:
        model = Customer
        fields = ('name','address','contactPerson','email','telNumber',)

class ProductForm(forms.ModelForm):
    # auto_id         = forms.AutoField(primary_key=True)
    name            = forms.CharField(max_length=100)
    description     = forms.CharField(max_length=100)
    unit            = forms.DecimalField(max_digits=8, decimal_places=0)
    unitCost        = forms.DecimalField(max_digits=8, decimal_places=0)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        pass

    class Meta:
        model = Product
        fields = ('name', 'description', 'unit','unitCost',)

class OrderForm(forms.ModelForm):
    # orderID is an AutoField in model
    customer    = forms.ModelChoiceField(queryset=Customer.objects.all(), to_field_name=None)
    product     = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.RadioSelect, help_text="Only choose one.")
    orderDate   = forms.DateField(widget=forms.SelectDateWidget)
    unit_sold   = forms.DecimalField(max_digits=9, decimal_places=0, help_text="max_digits = 9", min_value=1)
    costs       = forms.CharField(max_length=100, widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['unit_sold'].widget.attrs.update({'style':'background: green;'})
        pass

    class Meta:
        model = Order
        fields = ('customer', 'product', 'orderDate', 'unit_sold', 'costs',)

    # def cleaned_test_data(self):
    #     data = self.cleaned_data['name']
    #     return data

# class TestForm(forms.ModelForm):
#     name        = forms.CharField(max_length=100, help_text="Please enter letters only")
#     summary     = forms.CharField(required=False, widget=forms.Textarea(attrs={"message": "Please enter summary"})) #widget instance customize by instance param
#     customer    = forms.ModelChoiceField(queryset=Customer.objects.all(), to_field_name=None)#'name')
#     product     = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.RadioSelect, help_text="Only choose one.")
#     unit_sold   = forms.DecimalField(max_digits=9, decimal_places=0, help_text="max_digits = 9", min_value=1)
#     costs       = forms.CharField(max_length=100, widget=forms.HiddenInput(), required=False) 

#     summary.widget.attrs.update({'class': 'adding-css-class', 'style':'padding:10px;'}) #widget instance customize by instance .attrs.update({dict})

#     def __init__(self, *args, **kwargs):
#         super(TestForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update({'style':'background: green;'}) #widget instance customize by __init__ override
#         # self.fields['name'].widget.id_for_label(1)
#         # self.fields['name'].widget.get_context(name='name', value='value', attrs='attrs')

#         # self.fields['name'].widget = forms.widgets.Checkbox(attrs={'onclick': 'return false;'})
#         # self.fields['customer'].widget.attrs['onclick'] = 'return false;'
#         pass

#     class Meta:
#         model = TestModel
#         fields = ('name', 'summary', 'customer', 'product', 'unit_sold', 'costs',)

#     # def cleaned_test_data(self):
#     #     data = self.cleaned_data['name']
#     #     return data


from django import forms
from .models import Order, Customer, Product #, TestModel

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


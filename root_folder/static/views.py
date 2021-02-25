from django.shortcuts import render, get_object_or_404
from django.views import generic

from sales.models import Employee, Customer, Vendor, Product, Order#, TestModel

from django.http import HttpResponse
from sales.forms import CustomerForm, ProductForm, OrderForm

# Create your views here.
def index(request):
    """index page for whole project"""
    numEmployee = Employee.objects.all().count()
    numCustomer = Customer.objects.all().count()
    numVendor   = Vendor.objects.all().count()
    numProduct  = Product.objects.all().count()
    numOrder    = Order.objects.all().count()

    context = {
        'numEmployee': numEmployee,
        'numCustomer': numCustomer,
        'numVendor': numVendor,
        'numProduct': numProduct,
        'numOrder': numOrder,
    }

    return render(request, 'index.html', context=context)

class CustomerListView(generic.ListView):
    # print(Customer.objects.all().count())
    model = Customer
    #context_object_name = 'the_customer_list'

    # def get_queryset(self, **kwargs):
    #   context = super(, self).get_context_data(**kwargs)
    #   context['view_info'] = 'This is from views/CustomerListView'

class OrderListView(generic.ListView):
    # print(Order.objects.all().count())
    model = Order
    #context_object_name = 'the_order_list'

    # def get_queryset(self, **kwargs):
    #   context = super(, self).get_context_data(**kwargs)
    #   context['view_info'] = 'This is from views/OrderListView'

class ProductListView(generic.ListView):
    # print(Product.objects.all().count())
    model = Product
    #context_object_name = 'the_product_list'

    # def get_queryset(self, **kwargs):
    #   context = super(, self).get_context_data(**kwargs)
    #   context['view_info'] = 'This is from views/ProductListView'

class CustomerDetailView(generic.DetailView):
    model = Customer

class OrderDetailView(generic.DetailView):
    model = Order 

class ProductDetailView(generic.DetailView):
    model = Product

# def TestFormView(request):
#     if request.method == "POST":
#         form = TestForm(request.POST)
#         if form.is_valid():
#             name    = form.cleaned_data['name']
#             summary = form.cleaned_data['summary']
#             print(name, summary)
#             form = TestForm()
#             # model.save()

#     return render(request, 'form.html', {'form': form})

def CustomerFormView(request, id=None): # (id=None) reserve for editing customerform use
    if request.method == "POST":
        form = CustomerForm(request.POST)#, data)
        if form.is_valid():
            form.save()
            form = CustomerForm()
            # return redirect('/sales/')
    else: # For first time surf to the page or method=='GET'
        form = CustomerForm()
    return render(request, 'customerform.html', {'form': form})

def ProductFormView(request, id=None): # (id=None) reserve for editing customerform use
    if request.method == "POST":
        form = ProductForm(request.POST)#, data)
        if form.is_valid():
            form.save()
            form = ProductForm()
            # return redirect('/sales/')
    else: # For first time surf to the page or method=='GET'
        form = ProductForm()
    return render(request, 'productform.html', {'form': form})

def OrderFormView(request, id=None): # (id=None) reserve for editing orderform use
    model = Order.objects.all().count() + 1
    data = {'underscore_replace':'space'} # <label>Underscore replace</label><input=... value='space' />
    if request.method == "POST":
        form = OrderForm(request.POST)#, data)
        if form.is_valid():
            print(form.cleaned_data['product'].unitCost)
            if form.cleaned_data['unit_sold'] is not None:
                print(f"Not None: {form.cleaned_data['unit_sold']}")
                unitCost = form.cleaned_data['product'].unitCost * form.cleaned_data['unit_sold']
                new_form = form.save(commit=False)
                # https://youtu.be/qwE9TFNub84?t=743
                new_form.costs = str(unitCost) # Adding costs in new_form
                new_form.save()
            else:
                form.save()
            print(f'form:- {form.cleaned_data}')
            new_form.is_valid()
            print(f'new_form:- {new_form.cleaned_data}')
            form = OrderForm()
            # return redirect('/sales/')
    else: # For first time surf to the page or method=='GET'
        form = OrderForm()
    return render(request, 'orderform.html', {'form': form, 'model': model})







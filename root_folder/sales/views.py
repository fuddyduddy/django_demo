from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from sales.models import Employee, Customer, Vendor, Product, Order#, TestModel

from django.http import HttpResponse
from django.db.models import Max, Count
from sales.forms import CustomerForm, ProductForm, OrderForm
from sales.utils import render_to_pdf

from decimal import Decimal

from pprint import pprint

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

    def post(self, request, *args, **kwargs):
        content = self.model.objects.filter(pk=kwargs['pk']).values()[0]
        # print(content)
        # x = self.model.objects.filter(pk=kwargs['pk']).values()
        # print(type(x), "\n", dir(x), "\n", x)
        # print(request.path, args, kwargs)
        desired_objects = self.model.objects.get(pk=content['orderID'])
        content['customer'] = desired_objects.customer
        content['product'] = desired_objects.product
        content['product2'] = desired_objects.product2
        content['product3'] = desired_objects.product3
        totalsales = int(desired_objects.costs) + int(desired_objects.costs2) + int(desired_objects.costs3)
        content['totalsales'] = totalsales
        pdf = render_to_pdf('salesorderpdf.html', content)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "SalesOrder_%s.pdf" % ('123')
            content = "inline; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")
    
    def get_context_data(self, *args, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        self.order = self.get_object()
        context['queryset'] = Order.objects.values_list('costs', 'costs2', 'costs3')
        context['totalsales'] = int(context['order'].costs)+ int(context['order'].costs2)+ int(context['order'].costs3)
        # print(context['order'].costs, context['order'].costs2, context['order'].costs3)
        # print(type(context['order'].costs), type(context['order'].costs2), type(context['order'].costs3))
        # print(type(args), kwargs)
        # print(dir(Order.objects.values_list('costs').values))
        # print(Order.objects.values_list('costs').values)
        return context

class ProductDetailView(generic.DetailView):
    model = Product

# def TestFormView(request):
#     u = User.objects.get(username=request.user) 
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
            if form.cleaned_data['unitCost'] is not None:
                print(f"Not None: {form.cleaned_data['unitCost']}{type(form.cleaned_data['unitCost'])}")
                unitSalesPrice = Decimal(round(int(form.cleaned_data['unitCost']) * 1.05, 0))
                new_form = form.save(commit=False)  # From a Form object changed to <class 'sales.models.Product'>
                new_form.unitSalesprice = unitSalesPrice 
                new_form.save()
            else:
                form.save()
            print(f'form:- {form.cleaned_data}')
            print(f'new_form:- {new_form.unitSalesprice}{type(new_form)}') # <class 'sales.models.Product'>
            form = ProductForm()
    else:
        form = ProductForm()
    return render(request, 'productform.html', {'form': form})

def OrderFormView(request, id=None): # (id=None) reserve for editing orderform use
    def get_new_id():
        """ For First-time create form without record in database. 
            (Noted: the id will return to 1 if no record in database after first creation) """
        try:
            return int(str(Order.objects.all().last()))+1
        except:
            return 1
    new_id = get_new_id()
    data = {'underscore_replace':'space'} # <label>Underscore replace</label><input=... value='space' />
    queryset = Product.objects.all()  # <- this is queryset API
    if request.method == "POST":
        form = OrderForm(request.POST or None)#, data)
        if form.is_valid():
            # print(form.cleaned_data['product'].unitCost)
            print(f'pure form:- {form.cleaned_data}')
            if form.cleaned_data['unit_sold'] is not None:
                print(f"Not None: {form.cleaned_data['unit_sold']}")
                unitCost1 = form.cleaned_data['product'].unitSalesprice * form.cleaned_data['unit_sold']
                unitCost2 = form.cleaned_data['product'].unitSalesprice * form.cleaned_data['unit_sold2']
                unitCost3 = form.cleaned_data['product'].unitSalesprice * form.cleaned_data['unit_sold3']
                new_form = form.save(commit=False)
                # https://youtu.be/qwE9TFNub84?t=743
                new_form.costs = str(unitCost1) # Adding costs in new_form
                new_form.costs2 = str(unitCost2)
                new_form.costs3 = str(unitCost3)
                new_form.save()
            else:
                print(1)
                form.save()
            print(f'form:- {form.cleaned_data}')
            # new_form.is_valid()
            print(f'new_form:- {new_form.pk}')
            new_id += 1
            # form = OrderForm()
            return redirect('order-detail', new_form.pk)
        else:
            print(2)
            pass
            # return redirect('/sales/')
    else: # For first time surf to the page or method=='GET'
        print(3)
        form = OrderForm()
    # zipped_test = zip(form, queryset)
    # print(form.queryset)
    # print(dir(form.fields.get('product')))
    # print(type(form.fields.get('product')))
    return render(request, 'orderform.html', {'form': form, 'new_id': new_id, 'queryset': queryset})#, 'zipped_test':zipped_test})

def OrderConfirmView(request, **kwargs):
    form = kwargs
    return render(request, 'order-confirm', {'form':form})


# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse, HttpResponseNotFound

# def pdf_view(request):
#     fs = FileSystemStorage()
#     filename = 'mypdf.pdf'
#     if fs.exists(filename):
#         with fs.open(filename) as pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
#             return response
#             # This way the user will be prompted with the browser’s open/save file. If you want to display the PDF in the browser you can change the Content-Disposition to:
#             # response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
#     else:
#         return HttpResponseNotFound('The requested pdf was not found in our server.')







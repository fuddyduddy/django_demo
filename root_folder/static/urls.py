from django.urls import path
from . import views

from sales.views import (
    CustomerListView, 
    OrderListView, 
    ProductListView,
    CustomerDetailView,
    OrderDetailView,
    ProductDetailView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customer/<int:pk>', CustomerDetailView.as_view(),name='customer-detail'),
]

urlpatterns += [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>', OrderDetailView.as_view(),name='order-detail'),
]

urlpatterns += [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
]

urlpatterns += [
    path('customerform/', views.CustomerFormView, name="customer-form"),
    path('orderform/', views.OrderFormView, name="order-form"),
    path('productform/', views.ProductFormView, name="product-form"),
]
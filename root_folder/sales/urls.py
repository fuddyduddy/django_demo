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
    # Warning: '/' at beginning of path unneccesary, However, to ensure the pathway clear. Leave it be and pending for debugging.
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customer/<int:pk>', CustomerDetailView.as_view(),name='customer-detail'),
]

urlpatterns += [
    # Warning: '/' at beginning of path unneccesary, However, to ensure the pathway clear. Leave it be and pending for debugging.
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>', OrderDetailView.as_view(),name='order-detail'),
]

urlpatterns += [
    # Warning: '/' at beginning of path unneccesary, However, to ensure the pathway clear. Leave it be and pending for debugging.
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>', ProductDetailView.as_view(),name='product-detail'),
]

urlpatterns += [
    path('orderform/', views.OrderFormView, name="order-form"),
]
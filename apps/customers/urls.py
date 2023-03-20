from django.urls import path
from .views import (
    customer_list,
    customer_detail,
    CustomerCreateView,
    CustomerAccountDepositView,
    customer_account_detail,
)

app_name = 'customers'

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>/', customer_detail, name='customer_detail'),
    path('customer/account/<int:pk>/', customer_account_detail, name='customer_account'),
    path('customer/account/<int:pk>/deposit/', CustomerAccountDepositView.as_view(), name='customer_account_deposit'),
]

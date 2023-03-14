from django.contrib import admin
from .models import Customer, CustomerAccount, CustomerAccountDeposit


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'balance']
    list_filter = ['name']


@admin.register(CustomerAccount)
class CustomerAccountAdmin(admin.ModelAdmin):
    list_display = ['account_no', 'balance']
    list_filter = ['account_no']


@admin.register(CustomerAccountDeposit)
class CustomerAccountDepositAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'timestamp']

from decimal import Decimal
from django.db import models
from django.urls import reverse


class Customer(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=50, unique=True)
    #balance = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)
    
    def get_absolute_url(self):
        return reverse('customers:customer_detail', args=[self.pk]) # If error, change to self.id
    
    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return 0

    def __str__(self):
        return self.email
    

class CustomerAccount(models.Model):
    customer = models.OneToOneField(
        Customer,
        related_name='account',
        related_query_name='account',
        on_delete=models.CASCADE
    )
    account_no = models.PositiveIntegerField(unique=True)
    balance = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2
    )

    def get_absolute_url(self):
        return reverse('customers:customer_account', args=[self.pk])

    def __str__(self):
        return str(self.account_no)
    

class CustomerAccountDeposit(models.Model):
    """
    Model to register customers' deposits.
    """
    account = models.ForeignKey(
        CustomerAccount,
        related_name='deposits',
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    timestamp = models.DateTimeField(auto_now_add=True)
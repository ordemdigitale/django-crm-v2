from django import forms
from django.conf import settings
from django.db import transaction

from .models import Customer, CustomerAccount, CustomerAccountDeposit


class CustomerCreationForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = [
            'name',
            'email',
        ]
    
    @transaction.atomic # This to guarantee that either all of the transaction succeeds or none of it does.
    def save(self, commit=True):
        customer = super().save(commit=False)
        if commit:
            customer.save()

            CustomerAccount.objects.create(
                customer=customer,
                account_no=(
                    customer.id + settings.ACCOUNT_NUMBER_START_FROM
                )
            )


class CustomerAccountDepositForm(forms.ModelForm):
    """
    Form to handle Customer's deposit
    """
    class Meta:
        model = CustomerAccountDeposit
        fields = ['amount',]

    def save(self, commit=True):
        return super().save()
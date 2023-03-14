from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .models import Customer, CustomerAccount, CustomerAccountDeposit
from .forms import CustomerCreationForm, CustomerAccountDepositForm#, TransactionDateRangeForm


class CustomerCreateView(LoginRequiredMixin, CreateView):
    """
    CBV to create a new Customer.
    """
    model = Customer
    form_class = CustomerCreationForm
    template_name = 'customers/customer/create.html'

    def get_success_url(self):
        return reverse_lazy('customers:customer_list')


@login_required
def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }

    return render(request, 'customers/customer_list.html', context)


@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    #customer_account = get_object_or_404(CustomerAccount, pk=pk)
    customer_account = CustomerAccount.objects.get(pk=customer.account.id)
    #cart_product_form = CartAddProductForm()

    context = {
        'customer': customer,
        'customer_account': customer_account,
    #    'cart_product_form': cart_product_form
    }

    return render(request, 'customers/customer_detail.html', context)


@login_required
def customer_account_detail(request, pk):
    customer_account = get_object_or_404(CustomerAccount, pk=pk)

    context = {
        'customer_account': customer_account,
    }

    return render(request, 'customers/account_detail.html', context)


class CustomerAccountDepositView(LoginRequiredMixin, CreateView):
    model = CustomerAccountDeposit
    form_class = CustomerAccountDepositForm
    template_name = 'customers/deposit/create.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerAccountDepositView, self).get_context_data(**kwargs)
        context['account'] = get_object_or_404(CustomerAccount, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        form.instance.account = get_object_or_404(CustomerAccount, pk=self.kwargs['pk'])

        form.instance.account.balance += amount
        form.instance.account.save(
            update_fields=[
#                'initial_deposit_date',
                'balance'
            ]
        )

        return super(CustomerAccountDepositView, self).form_valid(form)

    def get_success_url(self):
        return reverse('customers:customer_account', kwargs={'pk': self.kwargs['pk'], })
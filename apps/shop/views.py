from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm


@login_required
def shop_index(request):
    #products = Product.objects.all()
    # Count the number of products in the databse
    product_count = Product.objects.count()

    context = {
    #    'products': products,
        'product_count': product_count,
    }

    return render(request, 'shop/shop_index.html', context)


@login_required
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'shop/product_list.html', context)


@login_required
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }

    return render(request, 'shop/product_detail.html', context)


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('shop:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shop:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                                        'quantity': item['quantity'],
                                        'override': True})
    return render(request, 'shop/cart_detail.html', {'cart': cart})
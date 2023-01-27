from .cart import Cart

def cart(request):
    return {'shop': Cart(request)}
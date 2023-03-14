from django.db import models
from apps.shop.models import Product
from apps.customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField()
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=80, null=True, blank=True)
    paid = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)
    
    def __str__(self):
        return f'Order #{self.id}'    
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_item', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
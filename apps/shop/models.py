from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id])

    def __str__(self):
        return self.name
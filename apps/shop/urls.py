from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_index, name='shop_index'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),

    path('panier/', views.cart_detail, name='cart_detail'),
    path('panier/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('panier/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
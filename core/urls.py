from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('customers/', include('apps.customers.urls', namespace='customsers')),
    path('orders/', include('apps.orders.urls', namespace='orders')),
    path('', include("apps.shop.urls", namespace='shop')),
    path("accounts/", include("apps.accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")), # django built-in auth
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
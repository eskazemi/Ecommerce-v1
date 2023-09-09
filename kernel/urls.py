from django.contrib import admin
from django.urls import (
    path,
    include,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('home', include("home.urls", namespace="home")),
    path('product/', include("product.urls", namespace="product")),
    path('orders/', include("orders.urls", namespace="orders")),
]

admin.site.site_header = 'Ecommerco'
admin.site.site_name = 'Ecommerco'

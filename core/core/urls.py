from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('home', include("home.urls", namespace="home")),
    path('product/', include("product.urls", namespace="product")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Ecommerco'
admin.site.site_name = 'Ecommerco'

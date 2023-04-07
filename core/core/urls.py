from django.contrib import admin
from django.urls import (
    path,
    include,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("accounts.urls", namespace="accounts")),
    path('home/', include("home.urls", namespace="home")),
]

admin.site.site_header = 'Ecommerco'
admin.site.site_name = 'Ecommerco'

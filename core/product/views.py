from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.views import View
from .models import Product


class ProductView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(is_available=True)
        return render(request, 'product/index.html', {"products": products})


class ProductDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'product/detail.html', {'product': product})


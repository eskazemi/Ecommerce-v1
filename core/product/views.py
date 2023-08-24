from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.views import View
from .models import (
    Product,
    Category,
)


class ProductView(View):
    def get(self, request, category_slug=None,  *args, **kwargs):
        products = Product.objects.filter(is_available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'product/index.html', {"products": products, "categories": categories})


class ProductDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'product/detail.html', {'product': product})




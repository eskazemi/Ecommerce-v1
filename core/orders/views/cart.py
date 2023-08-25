from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.views import View
from product.models import Product
from ..cart import Cart
from ..forms import (
    CartAddForm,
)
from django.contrib.auth.mixins import PermissionRequiredMixin


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {"cart": cart})


class CartAddView(PermissionRequiredMixin, View):
    permission_required = 'orders.add_order'

    def post(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product=product, quantity=form.cleaned_data["quantity"])
        return redirect('orders:cart')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove_session(product)
        return redirect('orders:cart')

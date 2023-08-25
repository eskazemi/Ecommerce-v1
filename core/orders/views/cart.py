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
from django.core.exceptions import PermissionDenied

class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {"cart": cart})


class CartAddView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('orders.add_order'):
            raise PermissionDenied()
        super().dispatch(request, *args, **kwargs)
        return redirect('orders:cart')

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

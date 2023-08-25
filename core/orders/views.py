from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.views import View
from product.models import Product
from .cart import Cart
from .models import (
    Order,
    OrderItem
)
from .froms import CartAddForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {"cart": cart})


class CartAddView(View):
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


class OrderCreateView(View, LoginRequiredMixin):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item["quantity"])
        cart.clear()
        return redirect('orders:order_detail', order.id)


class OrderDetailView(View, LoginRequiredMixin):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'orders/order.html', {"order": order})

from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.views import View
from .cart import Cart
from orders.models import (
    Order,
    OrderItem,
)
from orders.forms import (
    CouponForm,
)
from ..pay import (
    send_request,
    verify
)
from django.contrib.auth.mixins import LoginRequiredMixin


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
    form_class = CouponForm

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'orders/order.html', {"order": order, 'coupon': self.form_class})


class OrderPayView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        request.session["order_pay"] = {
            "order_id": order.id
        }
        send_request(order, request)


class OrderVerifyView(LoginRequiredMixin, View):
    def get(self, request):
        order_id = request.session["order_pay"]["order_id"]
        order = Order.objects.filter(id=int(order_id)).first()
        return verify(request.GET["Authority"], order)


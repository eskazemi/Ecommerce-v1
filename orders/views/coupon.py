from django.shortcuts import redirect
from django.views import View
from ..models import (
    Coupon,
    Order,
)
from ..forms import CouponForm
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class CouponView(LoginRequiredMixin, View):
    form_class = CouponForm

    def post(self, request, order_id, *args, **kwargs):
        now = datetime.now()
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            try:
                coupon = Coupon.objects.get(code__exact=code, expire_to__gt=now, active=True)

            except Coupon.DoesNotExist as e:
                messages.error(request, "this coupon DoseNotExist", 'danger')
                return redirect('orders:order_detail', order_id)
            order = Order.objects.get(id=order_id)
            order.discount = coupon.discount
            order.save()
            messages.success(request, "this is code", 'success')
        return redirect('orders:order_detail', order_id)

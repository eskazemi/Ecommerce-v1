from django.contrib import admin
from ..models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'code',
                    'expire_from',
                    'expire_to',
                    'discount',
                    'active',
                    )
    list_filter = ('active',)

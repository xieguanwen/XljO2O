import xadmin
from xiaolajiao.coupon.models import ECouponCat
from xiaolajiao.coupon.models import ElectronicCoupons

class ECouponCatAdmin(object):
    list_display = ("ECouponCatId","name")
    list_display_links = ("name",)
    # search_fields = ()

xadmin.site.register(ECouponCat,ECouponCatAdmin)


class ElectronicCouponsAdmin(object):
    list_display = ("electronicCouponsId","name")
    list_display_links = ("name",)
    # search_fields = ()

xadmin.site.register(ElectronicCoupons,ElectronicCouponsAdmin)



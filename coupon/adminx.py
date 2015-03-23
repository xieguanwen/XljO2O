import xadmin
from coupon.models import ECouponCat
from coupon.models import ElectronicCoupons

class ECouponCatAdmin(object):
    list_display = ("eCouponCatId","name")
    list_display_links = ("name",)
    # search_fields = ()

xadmin.site.register(ECouponCat,ECouponCatAdmin)


class ElectronicCouponsAdmin(object):
    list_display = ("electronicCouponsId","name")
    list_display_links = ("name",)
    # search_fields = ()

xadmin.site.register(ElectronicCoupons,ElectronicCouponsAdmin)



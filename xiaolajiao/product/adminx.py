import xadmin
from xiaolajiao.product.models import ProductSales
from xiaolajiao.product.models import ProductColor
from xiaolajiao.product.models import ProductType

class ProductSalesAdmin(object):
    list_display = ("productSalesId","imei","productName","addTime")
    list_display_links = ("productName",)
    # search_fields = ()

xadmin.site.register(ProductSales,ProductSalesAdmin)

class ProductColorAdmin(object):
    list_display = ("productColorId","colorValue")
    list_display_links = ("colorValue",)
    # search_fields = ()

xadmin.site.register(ProductColor,ProductColorAdmin)

class ProductTypeAdmin(object):
    list_display = ("tacCode","name")
    list_display_links = ("name",)
    # search_fields = ()

xadmin.site.register(ProductType,ProductTypeAdmin)
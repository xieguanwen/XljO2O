import xadmin
from xiaolajiao.product.models import ProductSales
from xiaolajiao.product.models import ProductColor

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
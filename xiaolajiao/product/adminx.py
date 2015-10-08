import xadmin
from xiaolajiao.product.models import ProductSales

class ProductSalesAdmin(object):
    list_display = ("productSalesId","productSn","productName","addTime")
    list_display_links = ("productName",)
    # search_fields = ()

xadmin.site.register(ProductSales,ProductSalesAdmin)
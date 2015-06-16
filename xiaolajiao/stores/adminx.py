import xadmin
from xiaolajiao.stores.models import Store
from xiaolajiao.stores.models import Clerk

class StoreAdmin(object):
    list_display = ("storeId","storeName")
    list_display_links = ("storeName",)
    search_fields = ("storeName",)

xadmin.site.register(Store,StoreAdmin)

class ClerkAdmin(object):
    list_display = ("clerkId","name")
    list_display_links = ("name",)
    search_fields = ("name",)

xadmin.site.register(Clerk,ClerkAdmin)

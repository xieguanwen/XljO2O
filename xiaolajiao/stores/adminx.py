import xadmin
from xiaolajiao.stores.models import Store
from xiaolajiao.stores.models import Clerk
from xiaolajiao.stores.models import StoreTemp
from xiaolajiao.stores.forms import StoresTempChangeForm


class StoreAdmin(object):
    list_display = ("storeId","storeName")
    list_display_links = ("storeName",)
    search_fields = ("storeName",)
    list_filter = ("status",)

xadmin.site.register(Store,StoreAdmin)

class StoreTempAdmin(object):
    list_display = ("storeId","storeName")
    list_display_links = ("storeName",)
    search_fields = ("storeName",)
    list_filter = ("status",)

    def get_model_form(self, **kwargs):
        if self.org_obj:
            self.form = StoresTempChangeForm
        return super(StoreTempAdmin, self).get_model_form(**kwargs)



xadmin.site.register(StoreTemp,StoreTempAdmin)

class ClerkAdmin(object):
    list_display = ("clerkId","name")
    list_display_links = ("name",)
    search_fields = ("name",)

xadmin.site.register(Clerk,ClerkAdmin)

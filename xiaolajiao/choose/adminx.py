import xadmin
from xiaolajiao.choose.models import SelectedTheme
from xiaolajiao.choose.models import ClerkAward
from xiaolajiao.choose.models import StoreAward

class SelectedThemeAdmin(object):
    list_display = ("selectedThemeId","name")
    list_display_links = ("name",)
    # search_fields = ()

xadmin.site.register(SelectedTheme,SelectedThemeAdmin)

class ClerkAwardAdmin(object):
    list_display = ("id","clerkId")
    list_display_links = ("clerkId",)
    # search_fields = ()

xadmin.site.register(ClerkAward,ClerkAwardAdmin)

class StoreAwardAdmin(object):
    list_display = ("storeAwardId","storeId")
    list_display_links = ("storeId",)
    # search_fields = ()

xadmin.site.register(StoreAward,StoreAwardAdmin)
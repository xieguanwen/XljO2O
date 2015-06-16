import xadmin
from xiaolajiao.region.models import Region
from mptt.admin import MPTTModelAdmin

class RegionAdmin(MPTTModelAdmin):
    list_display = ("regionId","name")
    list_display_links = ("name",)
    # search_fields = ()

xadmin.site.register(Region,RegionAdmin)
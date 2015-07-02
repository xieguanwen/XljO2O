import xadmin
from xiaolajiao.region.models import Region

class RegionAdmin(object):
    list_display = ("region_id","region_name")
    list_display_links = ("region_name",)
    # search_fields = ()

# xadmin.site.register(Region,RegionAdmin)
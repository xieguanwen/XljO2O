import xadmin
from xiaolajiao.region.models import Region

class RegionAdmin(object):
    list_display = ("regionId","name")
    list_display_links = ("name",)
    # search_fields = ()

# xadmin.site.register(Region,RegionAdmin)
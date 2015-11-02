import xadmin
from xiaolajiao.sncode.models import SnCode
from xiaolajiao.sncode.models import SnCodeAgents

class SnCodeAdmin(object):
    list_display = ("imei","agentsId")
    list_display_links = ("imei",)

    object_list_template = "sncode/sncode_list.html"

xadmin.site.register(SnCode,SnCodeAdmin)

class SnCodeAgentsAdmin(object):
    list_display = ("imei","agentsId")
    list_display_links = ("imei",)

xadmin.site.register(SnCodeAgents,SnCodeAgentsAdmin)

import xadmin
from xiaolajiao.sncode.models import SnCode
from xiaolajiao.sncode.models import SnCodeAgents

class SnCodeAdmin(object):
    list_display = ("imei","snCode")
    list_display_links = ("snCode",)

xadmin.site.register(SnCode,SnCodeAdmin)

class SnCodeAgentsAdmin(object):
    list_display = ("imei","snCode")
    list_display_links = ("snCode",)

xadmin.site.register(SnCodeAgents,SnCodeAgentsAdmin)

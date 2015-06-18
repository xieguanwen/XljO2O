import xadmin
from xiaolajiao.agents.models import Agents

class AgentsAdmin(object):
    list_display = ("agentsId","companyName")
    list_display_links = ("companyName",)
    search_fields = ("companyName","contact")
    raw_id_fields = ("userId",)


xadmin.site.register(Agents,AgentsAdmin)
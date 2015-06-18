import xadmin
from xiaolajiao.agents.models import Agents

class AgentsAdmin(object):
    list_display = ("agentsId","companyName")
    list_display_links = ("companyName",)
    search_fields = ("companyName","contact","User_userId")
    raw_id_fields = ("User",)


xadmin.site.register(Agents,AgentsAdmin)
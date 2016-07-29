import xadmin
from xiaolajiao.agents.models import Agents
from xiaolajiao.agents.models import MultiAgents
from xiaolajiao.agents.models import Supervise

class AgentsAdmin(object):
    list_display = ("agentsId","companyName")
    list_display_links = ("companyName",)
    search_fields = ("companyName","contact")
    raw_id_fields = ("userId",)

class MultiAgentsAdmin(object):
    list_display = ("multiAgentsId","name")
    list_display_links = ("name",)
    search_fields = ("name",)

class SuperviseAdmin(object):
    list_display = ("superviseId","name")
    list_display_links = ("name",)
    search_fields = ("name",)


xadmin.site.register(Agents,AgentsAdmin)
xadmin.site.register(MultiAgents,MultiAgentsAdmin)
xadmin.site.register(Supervise,SuperviseAdmin)
import xadmin
from xiaolajiao.sncode.models import SnCode
from xiaolajiao.sncode.models import SnCodeAgents
from xiaolajiao.sncode.forms import SnCodeAgentsChangeForm

class SnCodeAdmin(object):
    list_display = ("imei","agentsId")
    list_display_links = ("imei",)

    object_list_template = "sncode/sncode_list.html"

xadmin.site.register(SnCode,SnCodeAdmin)

class SnCodeAgentsAdmin(object):
    list_display = ("imei","agentsId")
    list_display_links = ("imei",)
    search_fields = ("imei",)

    def get_model_form(self, **kwargs):
        if self.org_obj is not None:
            self.form = SnCodeAgentsChangeForm
        return super(SnCodeAgentsAdmin, self).get_model_form(**kwargs)

xadmin.site.register(SnCodeAgents,SnCodeAgentsAdmin)

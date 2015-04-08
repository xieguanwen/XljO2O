import xadmin
from xiaolajiao.active.models import ActiveTemplate
from xiaolajiao.active.models import Active
from xiaolajiao.active.models import ActiveTop

class ActiveTemplateAdmin(object):
    list_display = ("activeTemplateId","name")
    list_display_links = ("name",)
    # search_fields = ()

xadmin.site.register(ActiveTemplate,ActiveTemplateAdmin)

class ActiveAdmin(object):
    list_display = ("activeId","subject")
    list_display_links = ("subject",)
    # search_fields = ()

xadmin.site.register(Active,ActiveAdmin)

class ActiveTopAdmin(object):
    list_display = ("activeTopId","activeId")
    list_display_links = ("activeId",)
    # search_fields = ()

xadmin.site.register(ActiveTop,ActiveTopAdmin)

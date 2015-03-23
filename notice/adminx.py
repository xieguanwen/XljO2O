import xadmin
from xadmin import views

class MainDashboard(object):
    widgets = [
    ]
xadmin.site.register(views.website.IndexView, MainDashboard)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)


# class GlobalSetting(object):
#     global_search_models = [Host, IDC]
#     global_models_icon = {
#         # Host: 'fa fa-laptop', IDC: 'fa fa-cloud'
#     }
#     menu_style = 'default'#'accordion'
# xadmin.site.register(views.CommAdminView, GlobalSetting)

# xadmin.site.register(AccessRecord, AccessRecordAdmin)

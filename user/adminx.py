import xadmin
from xadmin import views
from models import User
from stores.models import Store
from agents.models import Agents

# class MainDashboard(object):
#     widgets = [
#     ]
# xadmin.site.register(views.website.IndexView, MainDashboard)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSetting(object):
    global_search_models = [User, Store , Agents]
    global_models_icon = {
        User: 'fa fa-laptop', Store: 'fa fa-cloud'
    }
    menu_style = 'default'
xadmin.site.register(views.CommAdminView, GlobalSetting)


class UserAdmin(object):
    list_display = ("userId","userName")
    list_display_links = ("userName",)
    search_fields = ("userName",)

xadmin.site.register(User,UserAdmin)
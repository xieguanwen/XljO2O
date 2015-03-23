import xadmin
from xadmin import views
from django.contrib import admin
from models import User

# class MainDashboard(object):
#     widgets = [
#     ]
# xadmin.site.register(views.website.IndexView, MainDashboard)


# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True
# xadmin.site.register(views.BaseAdminView, BaseSetting)

class UserAdmin(object):
    list_display = ("userId","userName")
    list_display_links = ("userName",)
    search_fields = ("userName",)

xadmin.site.register(User,UserAdmin)
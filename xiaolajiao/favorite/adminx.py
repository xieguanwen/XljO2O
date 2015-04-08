import xadmin
from xiaolajiao.favorite.models import Favorite

class FavoriteAdmin(object):
    list_display = ("favoriteId","user_id")
    list_display_links = ("user_id",)
    # search_fields = ()

xadmin.site.register(Favorite,FavoriteAdmin)


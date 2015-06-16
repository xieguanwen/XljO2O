import xadmin
from xiaolajiao.comment.models import StoreComment
from xiaolajiao.comment.models import ActiveComment


class ActiveCommentAdmin(object):
    list_display = ("activeCommentId","subject")
    list_display_links = ("subject",)
    # search_fields = ("subject",)

xadmin.site.register(ActiveComment,ActiveCommentAdmin)

class StoreCommentAdmin(object):
    list_display = ("storeCommentId","subject")
    list_display_links = ("subject",)

xadmin.site.register(StoreComment,StoreCommentAdmin)
import xadmin
from xiaolajiao.comment.models import Comment

class CommentAdmin(object):
    list_display = ("commentId","subject")
    list_display_links = ("subject",)
    # search_fields = ()

xadmin.site.register(Comment,CommentAdmin)
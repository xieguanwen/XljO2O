import xadmin
from notice.models import NoticeCat
from notice.models import Notice

class NoticeCatAdmin(object):
    list_display = ("noticeCatId","name")
    list_display_links = ("name",)
    # search_fields = ()

xadmin.site.register(NoticeCat,NoticeCatAdmin)

class NoticeAdmin(object):
    list_display = ("noticeId","subject")
    list_display_links = ("subject",)
    # search_fields = ()

xadmin.site.register(Notice,NoticeAdmin)



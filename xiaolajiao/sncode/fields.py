from django.db.models.fields.related import ForeignKey
from django.db.models.fields.related import ManyToOneRel

class MyForeignKey(ForeignKey):
    def __init__(self, to, to_field=None, rel_class=ManyToOneRel,db_constraint=True, **kwargs):
        super(MyForeignKey,self).__init__(to, to_field=None, rel_class=ManyToOneRel,db_constraint=True, **kwargs)

    # @property
    # def related_field(self):
    #     print(super(MyForeignKey.related_field))
    #     fieldValue = super(MyForeignKey,self).related_field()
    #     print("_________________________________________")
    #     if(fieldValue is None):
    #         return 0
    #     return fieldValue

    def get_default(self):
        value = super(MyForeignKey,self).get_default()
        print("_________________________________________")
        if(value is None or value == ""):
            return 0
        return value
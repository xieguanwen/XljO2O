from django.db import connection

class StoreData(object):
    endDate = ''
    startDate = ''
    cursor = None
    province = {}

    def __init__(self,startDate,endDate):
        self.endDate = endDate
        self.startDate = startDate
        self.cursor = connection.cursor()

    def __new__(cls, *args, **kwargs):
        super.__new__(cls,*args)


    def todayRecord(self):
        sql = """select * from province as p LEFT JOIN store as s ON p.province = s.province WHERE s.status = 1 and s.addTime >= %s ;"""
        param = [self.endDate]
        cursor = connection.cursor()
        cursor.execute(sql,param)
        row = cursor.fetchall()

    def province(self):
        pass





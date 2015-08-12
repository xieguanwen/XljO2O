import datetime
from django.db import connection
from xiaolajiao.region.models import Province
from xiaolajiao.agents.models import Agents

class StoreData(object):
    endDate = ''
    startDate = ''
    cursor = None
    total = dict()
    data = list()

    def __init__(self,startDate,endDate):
        self.data = list()
        self.cursor = None
        self.startDate = startDate
        self.endDate = endDate
        self.cursor = connection.cursor()

    def todayRecord(self):
        sql = """select * from province as p LEFT JOIN store as s ON p.province = s.province WHERE s.status = 1 and s.addTime >= %s ;"""
        param = [self.endDate]
        self.cursor.execute(sql,param)
        row = self.cursor.fetchall()

    def province(self):
        return Province.objects.filter(region_type=1)

    def getStatistics(self):
        provinces = self.province()
        for province in provinces:
            pdict = dict()
            pdict.setdefault("province",province.province)
            pdict.setdefault("provinceName",province.region_name)
            pdict.setdefault("numberOfCity",self.numberOfCity(province.province))
            pdict.setdefault("numberOfTowns",self.numberOfTowns(province.province))
            pdict.setdefault("numberOfStores",self.numberOfStores(province.province))
            pdict.setdefault("newStores",self.newStores(province.province))
            pdict.setdefault("newCity",self.newCity(province.province))
            pdict.setdefault("newTown",self.newTown(province.province))
            self.data.append(pdict)
        return self.data

    def numberOfCity(self,provinceId):
        sql = """SELECT c.city FROM city as c,store as s WHERE c.city = s.city AND c.province = %s AND s.addTime>%s AND s.addTime<%s GROUP BY c.city;"""
        param = [provinceId,self.startDate,self.endDate]
        rows = self.__querySql(sql,param)
        return len(rows)

    def numberOfTowns(self,provinceId):
        sql = """SELECT r.region FROM city as c,region as r,store as s WHERE r.city = c.city AND r.region = s.region AND s.province = %s AND s.addTime>%s AND s.addTime<%s GROUP BY r.region;"""
        param = [provinceId,self.startDate,self.endDate]
        rows = self.__querySql(sql,param)
        return len(rows)

    def numberOfStores(self,provinceId):
        sql = """SELECT count(*) FROM store as s WHERE s.province = %s AND s.status = 1 AND s.addTime>%s AND s.addTime<%s;"""
        param = [provinceId,self.startDate,self.endDate]
        self.cursor.execute(sql,param)
        row = self.cursor.fetchone()
        return row[0]

    def newStores(self,provinceId):
        sql = """SELECT count(*) FROM store as s WHERE s.province = %s AND s.addTime>%s AND s.addTime<%s;"""
        param = [provinceId,self.startDate,self.endDate]
        self.cursor.execute(sql,param)
        row = self.cursor.fetchone()
        return row[0]

    def newCity(self,provinceId):
        sql = """SELECT c.city FROM city as c,store as s WHERE c.city = s.city AND c.province = %s AND s.addTime>%s AND s.addTime<%s GROUP BY c.city;"""
        param = [provinceId,self.startDate,self.endDate]
        rowAll = self.__querySql(sql,param)
        sqlNew = """SELECT c.city FROM city as c,store as s WHERE c.city = s.city AND c.province = %s AND s.addTime<%s GROUP BY c.city;"""
        param = [provinceId,self.startDate]
        rowOld = self.__querySql(sqlNew,param)
        list1 = list()
        list2 = list()
        for row in rowAll:
            list1.append(row[0])
        for row in rowOld:
            list2.append(row[0])
        return len(list(set(list1).difference(list2)))

    def newTown(self,provinceId):
        sql = """SELECT r.region FROM city as c,region as r,store as s WHERE r.city = c.city AND r.region = s.region AND s.province = %s AND s.addTime>%s AND s.addTime<%s GROUP BY r.region;"""
        param = [provinceId,self.startDate,self.endDate]
        rowAll = self.__querySql(sql,param)

        sql = """SELECT r.region FROM city as c,region as r,store as s WHERE r.city = c.city AND r.region = s.region AND s.province = %s AND s.addTime<%s GROUP BY r.region;"""
        param = [provinceId,self.startDate]
        rowOld = self.__querySql(sql,param)

        list1 = list()
        list2 = list()
        for row in rowAll:
            list1.append(row[0])
        for row in rowOld:
            list2.append(row[0])
        return len(list(set(list1).difference(list2)))

    def total(self):
        pass

    def __querySql(self,sql,param):
        self.cursor.execute(sql,param)
        row = self.cursor.fetchall()
        return row

class AgentsData(object):
    cursor = None
    data = list()
    toDay = None

    def __init__(self):
        self.data = list()
        self.cursor = connection.cursor()
        self.toDay = datetime.datetime.today()

    def statisticsAgents(self):
        agents = Agents.objects.filter(status=1)
        for agent in agents:
            aDict = dict()
            aDict.setdefault("agentsName",agent.companyName)
            aDict.setdefault("numberOfStores",self.numberOfStores(agent.agentsId))
            aDict.setdefault("increasingOfStores",self.increaseOfStores(agent.agentsId))
            aDict.setdefault("weekIncreaseOfStores",self.increaseOfStores(agent.agentsId,7))
            aDict.setdefault("monthIncreaseOfStores",self.increaseOfStores(agent.agentsId,30))
            self.data.append(aDict)
        return self.data

    def numberOfStores(self,agentsId):
        sql = """ SELECT COUNT(*) FROM store WHERE agentsId = %s AND status = 1"""
        param = [agentsId]
        return self.sqlQueryOne(sql,param)

    def increaseOfStores(self,agentsId,days = 1):
        sql = """ SELECT COUNT(*) FROM store WHERE agentsId = %s AND status = 1 AND addTime>%s AND addTime<%s"""
        param = [agentsId,self.toDay,(self.toDay+datetime.timedelta(days))]
        return self.sqlQueryOne(sql,param)

    def sqlQueryOne(self,sql,param):
        self.cursor.execute(sql,param)
        row = self.cursor.fetchone()
        return row[0]


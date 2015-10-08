from django.db import models
from xiaolajiao.agents.models import Agents
from xiaolajiao.stores.models import Store
from xiaolajiao.stores.models import Clerk
import datetime

class ProductSales(models.Model):
    productSalesId = models.AutoField("产品销售编号",primary_key=True)
    productSn = models.CharField("网标料号",max_length=100)
    productModel = models.CharField("入网型号",max_length=100)
    productName = models.CharField("设备名称",max_length=100)
    agentsId = models.ForeignKey(Agents,db_column="agentsId",verbose_name="代理商")
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    clerkId = models.ForeignKey(Clerk,db_column="clerkId",verbose_name="店员")
    tacCode = models.CharField("TAC",max_length=100)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())

    def __unicode__(self):
        return self.productName

    class Meta():
        db_table = "product_sales"
        app_label = "product"
        verbose_name = "产品销售"
        verbose_name_plural = "产品销售"

from django.db import models
from xiaolajiao.agents.models import Agents
from xiaolajiao.stores.models import Store
from xiaolajiao.stores.models import Clerk
import datetime

class ProductSales(models.Model):
    productSalesId = models.AutoField("��Ʒ���۱��",primary_key=True)
    productSn = models.CharField("�����Ϻ�",max_length=100)
    productModel = models.CharField("�����ͺ�",max_length=100)
    productName = models.CharField("�豸����",max_length=100)
    agentsId = models.ForeignKey(Agents,db_column="agentsId",verbose_name="������")
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="����")
    clerkId = models.ForeignKey(Clerk,db_column="clerkId",verbose_name="��Ա")
    tacCode = models.CharField("TAC",max_length=100)
    addTime = models.DateTimeField("���ʱ��",default=datetime.datetime.now())

    def __unicode__(self):
        return self.productName

    class Meta():
        db_table = "product_sales"
        app_label = "product"
        verbose_name = "��Ʒ����"
        verbose_name_plural = "��Ʒ����"

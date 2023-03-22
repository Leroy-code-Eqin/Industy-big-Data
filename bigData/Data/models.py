from django.db import models

# Create your models here.
class Data1(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    岗位 = models.CharField(max_length=32, blank=True, null=True)
    地点 = models.CharField(max_length=32, blank=True, null=True)
    薪资 = models.CharField(max_length=32, blank=True, null=True)
    工作经验 = models.CharField(max_length=32, blank=True, null=True)
    学历 = models.CharField(max_length=32, blank=True, null=True)
    公司 = models.CharField(max_length=32, blank=True, null=True)
    技能 = models.CharField(max_length=32, blank=True, null=True)
    区间最小薪资千 = models.IntegerField(db_column='区间最小薪资千', blank=True, null=True)
    城市地区 = models.CharField(max_length=32, blank=True, null=True)
    城市 = models.CharField(max_length=32, blank=True, null=True)
    地区 = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data1'
        verbose_name = "Python岗位数据"
        verbose_name_plural = "Python岗位数据"



    def str(self):
        return str(self.id)
class Search(models.Model):
    岗位 = models.CharField(max_length=255, blank=True, null=True)
    地点 = models.CharField(max_length=32, blank=True, null=True)
    薪资 = models.CharField(max_length=32, blank=True, null=True)
    工作经验 = models.CharField(max_length=32, blank=True, null=True)
    学历 = models.CharField(max_length=32, blank=True, null=True)
    公司 = models.CharField(max_length=32, blank=True, null=True)
    技能 = models.CharField(max_length=32, blank=True, null=True)
    区间最小薪资千 = models.IntegerField(db_column='区间最小薪资千', blank=True, null=True)
    城市地区 = models.CharField(max_length=32, blank=True, null=True)
    城市 = models.CharField(max_length=32, blank=True, null=True)
    地区 = models.CharField(max_length=32, blank=True, null=True)
    class Meta:
        managed =True
        db_table = 'search'





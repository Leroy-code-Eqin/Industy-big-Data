from .models import Search
def addsearch(i):
   Search.objects.create(
       岗位=i.岗位,
       地点=i.地点,
       薪资=i.薪资,
       工作经验=i.工作经验,
       学历=i.学历,
       公司=i.公司,
       技能=i.技能,
       区间最小薪资千=i.区间最小薪资千,
       城市地区=i.城市地区,
       城市=i.城市,
       地区=i.地区,
		)

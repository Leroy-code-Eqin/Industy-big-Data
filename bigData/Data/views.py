from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from . import service
from  django.shortcuts import render
from .models import Data1
from .models import Search
import pandas as pd

# from .searchFun import start_search
def searchPage(request):
     return render(request, 'index.html')
def respond(request):
    text=request.POST['搜索内容']
    db=Data1.objects.all()
    po_list=[]
    for i in db:
         if text in i.岗位:
             service.addsearch(i)
    df = pd.read_excel("中国城市经纬度数据表.xlsx")
    from django.db import connection
    sql = "select 工作经验,count(*) as b from search group by 工作经验 order by b desc "
    with connection.cursor() as cur:
        cur.execute(sql)
    data_list = cur.fetchall()
    sql = "select 学历,avg(区间最小薪资千) as b from data1 group by 学历 order by b desc"
    with connection.cursor() as cur:
        cur.execute(sql)
    data_list1 = cur.fetchall()
    sql = "select 岗位 as b from search "
    with connection.cursor() as cur:
        cur.execute(sql)
    data_list2 = cur.fetchall()
    sql = "select 技能  from search"
    with connection.cursor() as cur:
        cur.execute(sql)
    data_list3 = cur.fetchall()
    sql = "select 城市,avg(区间最小薪资千) as b from data1  group by 城市 order by b desc "
    with connection.cursor() as cur:
        cur.execute(sql)
    data_list5 = cur.fetchall()
    sql = "select 公司,count(*) as b,round(avg(区间最小薪资千),1) as b from search  group by 公司 order by b desc"
    with connection.cursor() as cur:
        cur.execute(sql)
    data_list6 = cur.fetchall()
    x_bar1=[]
    y_bar1=[]
    x_bar2 = []
    y_bar2 = []
    for i in  data_list:
        x_bar1.append(i[0])
        y_bar1.append(round(i[1],1))

    for i in  data_list1:
        x_bar2.append(i[0])
        y_bar2.append(round(i[1],1))

    list1 = []
    for i in data_list2:
        a = i[0].split(";")

        for j in i[0].split(";"):
            j = j.replace('python', 'Python')
            j = j.replace('Python开发工程师', 'Python开发')
            list1.append(j)
    dict = {}
    for key in list1:
        dict[key] = dict.get(key, 0) + 1
    a1 = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    s_pie= []
    for i in a1[0:6]:
        s_pie.append({"name": i[0], "value": i[1]})

    list1 = []
    for i in data_list3:
        a = i[0].split(";")
        for j in i[0].split(";"):
            j = j.replace('[', '')
            j = j.replace(']', '')
            j = j.replace(' ', '')
            j = j.replace("'", '')
            list1.append(j)
    dict = {}
    for key in list1:
        dict[key] = dict.get(key, 0) + 1
    a1 = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    s_pie2 = []
    for i in a1[0:6]:
        s_pie2.append({"name": i[0], "value": i[1]})
    map=[]
    for i in data_list5:
        for j in df.itertuples():
            if i[0] == j[1]:
                map.append({"name": i[0], "value": [j[3], j[2], i[1]]})
    print(map)
    table = []
    for i in data_list6[0:10]:
        table.append({"name": i[0], "value1": i[1], "value2": i[2]})
    data_bar1={
        "x_bar1":x_bar1,
        "y_bar1":y_bar1,
        "x_bar2": x_bar2,
        "y_bar2": y_bar2,
        "s_pie" :s_pie,
        "s_pie2": s_pie2,
        "map":map,
        "table":table
    }

    return render(request, 'result.html', data_bar1)

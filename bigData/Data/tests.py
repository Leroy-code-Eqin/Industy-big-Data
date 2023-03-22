from pyecharts.charts import Geo,Map,Bar, Line, Page,Pie, Boxplot, WordCloud
from pyecharts.globals import ThemeType
from pyecharts.charts import Scatter
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Pie
import sqlite3
from pyecharts import options as opts
from pyecharts.charts import Bar

from pyecharts.components import Table
def map1():
    con= sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    sql = "select 城市,avg(区间最小薪资_k_field) as b from app_data2  group by 城市 order by b desc "
    #sql='select * from myapp_two_data2'
    #sql = "select 城市,avg(区间最小薪资_k_field) as b from app_data2 group by 城市 order by b desc "
    cur.execute(sql)
    data_list = cur.fetchall()
    print(data_list[1])

    c = (
    Map(init_opts=opts.InitOpts(chart_id=2, theme=ThemeType.DARK,))
    .add("", data_list, "china",
          label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Python岗位地区分布图", pos_left='center',title_textstyle_opts=(opts.TextStyleOpts(font_size=20,font_family="STXihei"))),
        visualmap_opts=opts.VisualMapOpts(max_=20,is_piecewise=True)
    )

    )
    return c

def pie():
    con= sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    sql = "select 技能  from app_data2 "
    #sql='select * from myapp_two_data2'
    #sql = "select 城市,avg(区间最小薪资_k_field) as b from app_data2 group by 城市 order by b desc "
    cur.execute(sql)
    data_list = cur.fetchall()
    list1=[]
    for i in data_list:
        a=i[0].split(";")

        for j in i[0].split(";"):
            j=j.replace('[', '')
            j=j.replace(']', '')
            j = j.replace(' ', '')
            j = j.replace("'", '')
            list1.append(j)

    print(list1)
    dict={}
    for key in list1:
        dict[key]=dict.get(key,0)+1

    a1 = sorted(dict.items(),key = lambda x:x[1],reverse = True)


    c = (
        Pie(init_opts=opts.InitOpts(chart_id=1, theme=ThemeType.DARK,))
        .add("", a1[0:6],
             center=["50%", "60%"],
             radius=["40%", "75%"],
             rosetype="area"
             )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left='right', orient='vertical',is_show=False) ,
            title_opts=opts.TitleOpts(title="岗位技能需求占比图", pos_left='center',
                                      title_textstyle_opts=(opts.TextStyleOpts(font_size=20, font_family="STXihei"))),

        )
    )
    return c

def pie1():
    con= sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    sql = "select 岗位 as b from app_data2  "
    #sql='select * from myapp_two_data2'
    #sql = "select 城市,avg(区间最小薪资_k_field) as b from app_data2 group by 城市 order by b desc "

    cur.execute(sql)
    data_list = cur.fetchall()
    list1=[]
    for i in data_list:
        a = i[0].split(";")

        for j in i[0].split(";"):
            j = j.replace('python', 'Python')
            j = j.replace('Python开发工程师', 'Python开发')
            list1.append(j)

    print(list1)
    dict = {}
    for key in list1:
        dict[key] = dict.get(key, 0) + 1

    a1 = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    c = (
        Pie(init_opts=opts.InitOpts(chart_id=7, theme=ThemeType.DARK,))
        .add("", a1[0:6],
             center=["50%", "60%"],
             radius=["40%", "75%"],
             rosetype="area"
             )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left='right', orient='vertical',is_show=False) ,
            title_opts=opts.TitleOpts(title="招聘岗位种类占比图", pos_left='center',
                                      title_textstyle_opts=(opts.TextStyleOpts(font_size=20, font_family="STXihei"))),

        )
    )
    return c

def bar1():
    con= sqlite3.connect("db.db3")
    cur = con.cursor()
    #sql = "select 技能  from app_data2 "
    #sql='select * from myapp_two_data2'
    sql = "select 工作经验,count(*) as b from app_data2 group by 工作经验 order by b desc "
    cur.execute(sql)
    data_list = cur.fetchall()

    x=[]
    y=[]
    for i in  data_list:
        x.append(i[0])
        y.append(round(i[1],1))
        print(y)

    c = (
        Bar(init_opts=opts.InitOpts(chart_id=3,  theme=ThemeType.DARK,))
        .add_xaxis(x)
        .add_yaxis("岗位数",y, stack="stack1",category_gap="50%")

        .set_series_opts(label_opts=opts.LabelOpts(is_show=False, position="top", font_size=12, color='＃D3D3D3'),
                         markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="min", name="最小值"),
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="average", name="平均值"),
            ]
        ),)
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left='right'),
                         title_opts=opts.TitleOpts(title="招聘岗位工作经验区间分布", pos_left='center',title_textstyle_opts=(opts.TextStyleOpts(font_size=20,font_family="STXihei"))),
                         xaxis_opts=opts.AxisOpts(type_='category',

                                                  axislabel_opts=opts.LabelOpts(
                                                      rotate=0),
                                                  ),
                        yaxis_opts=opts.AxisOpts(name="岗位数",
                                                    axislabel_opts={"rotate": 0},
                                                    splitline_opts=opts.SplitLineOpts(is_show=True,
                                                    linestyle_opts=opts.LineStyleOpts(type_='solid'),
                                                                                      ),
    ),

    )

    )
    return c



def bar2():
    con= sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    #sql = "select 技能  from app_data2 "
    #sql='select * from myapp_two_data2'
    sql = "select 学历,avg(区间最小薪资_k_field) as b from app_data2 group by 学历 order by b desc"
    cur.execute(sql)
    data_list = cur.fetchall()
    print(data_list)
    x=[]
    y=[]
    for i in  data_list:
        x.append(i[0])
        y.append(round(i[1],1))

    c = (
        Bar(init_opts=opts.InitOpts(chart_id=4, theme=ThemeType.DARK,))
        .add_xaxis(x)
        .add_yaxis("薪资水平",y, stack="stack1",category_gap="50%")


        .set_series_opts(label_opts=opts.LabelOpts(is_show=False, position="inside", font_size=12, color='#FFFFFF',),
                         markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="min", name="最小值"),
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="average", name="平均值"),
            ]
        ),)
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left='right'),
                         title_opts=opts.TitleOpts(title="招聘学历-薪资分布图", pos_left='center',title_textstyle_opts=(opts.TextStyleOpts(font_size=20,font_family="STXihei"))),
                         xaxis_opts=opts.AxisOpts(type_='category',
                                                  name="学历",
                                                  axislabel_opts=opts.LabelOpts(
                                                      rotate=45),),
                         yaxis_opts=opts.AxisOpts(name="薪资",
                                                 axislabel_opts={"rotate": 0},
                                                 splitline_opts=opts.SplitLineOpts(is_show=True,
                                                 linestyle_opts=opts.LineStyleOpts(type_='solid'),
                                                                                      ),)

    ))

    return c
def table1(table_color = '#333333'):
	con= sqlite3.connect("db.sqlite3")
	cur = con.cursor()
	sql = "select 公司,count(*) as b,round(avg(区间最小薪资_k_field),1) as b from app_data2  group by 公司 order by b desc "
	#sql='select * from myapp_two_data2'
	#sql = "select 城市,avg(区间最小薪资_k_field) as b from app_data2 group by 城市 order by b desc "
	cur.execute(sql)
	data_list = cur.fetchall()
	print(data_list[1])
	table = (
		Table(page_title='我的表格标题' )
			.add(headers=['公司', '岗位数', '平均薪资'], rows=data_list[0:10], attributes={
			"align": "left",
			"border": False,
			"padding": "20px",
			"style": "background:{}; width:450px; height:350px; font-size:10px; color:#C0C0C0;padding:3px;".format(table_color)
		})
			.set_global_opts(title_opts=opts.TitleOpts(title='这是表格1'))
	)
	return table

def table2(table_color = '#333333'):
	table = Table()
	table.add(headers=["python岗位数据看板"], rows=[], attributes={
		"align": "center",
		"border": False,
		"padding": "2px",
		"style": "background:{}; width:1350px; height:50px; font-size:25px; color:#C0C0C0;".format(table_color)
	})
	return table


# 执行之前,请确保:1、已经把json文件放到本目录下 2、把json中的title和table的id替换掉

def tab1(name,color): #作为标题吧
    c = (Pie().
        set_global_opts(
        title_opts=opts.TitleOpts(title=name,pos_left='center',pos_top='center',
                                title_textstyle_opts=opts.TextStyleOpts(color=color,font_size=35))))
    return c
#page = Page(page_title="基于Python的电影数据分析大屏",layout=Page.DraggablePageLayout, )
page = Page( )
page.save_resize_html(
	source="test.html",
	cfg_file="chart_config (3).json",
	dest="result.html"
)

# 在页面中添加图表
page.add(
    table2(),

    table1(),
    map1(),
    bar1(),
    #bar4(),
    bar2(),
    pie1(),
    pie(),)

page.render('test.html')

"""from bs4 import BeautifulSoup
with open("test.html", "r+", encoding='utf-8') as html:
    html_bf = BeautifulSoup(html, 'lxml')
    divs = html_bf.select('.chart-container')
    divs[0]["style"] = "width:40%;height:10%;position:absolute;top:0;left:30%;"
    divs[1]["style"] = "width:40%;height:40%;position:absolute;top:10%;left:30%;"
    divs[2]["style"] = "width:40%;height:50%;position:absolute;top:50%;left:30%;"
    divs[3]["style"] = "width:30%;height:50%;position:absolute;top:0;left:0;"
    divs[4][ "style"] = "width:30%;height:50%;position:absolute;top:50%;left:0;"
    divs[5]["style"] = "width:30%;height:50%;position:absolute;top:0;left:70%;"
    divs[6]['style'] = "width:30%;height:50%;position:absolute;top:50%;left:70%;"
    body = html_bf.find("body")
    body["style"] = "background-color:#FFFFFF;"  # 背景颜色
    html_new = str(html_bf)
    html.seek(0, 0)
    html.truncate()
    html.write(html_new)
    html.close()
"""


from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode


fn = """
    function(params) {
        if(params.name == '其他')
            return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
        return params.name + ' : ' + params.value + '%';
    }
    """


def new_label_opts():
    return opts.LabelOpts(formatter=JsCode(fn), position="center")


c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["剧情", "其他"], [25, 75])],
        center=["20%", "30%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["奇幻", "其他"], [24, 76])],
        center=["55%", "30%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["爱情", "其他"], [14, 86])],
        center=["20%", "70%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["惊悚", "其他"], [11, 89])],
        center=["55%", "70%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-多饼图基本示例"),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
        ),
    )
    #.render("mutiple_pie.html")
)
c.render_notebook()

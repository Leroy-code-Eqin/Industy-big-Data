from django.contrib import admin
admin.site.site_header = '数据管理页面'
admin.site.site_title = '数据管理后端'
admin.site.index_title = '职业数据'
# Register your models here.
from .models import Data1
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('岗位', '薪资','地点','学历','工作经验')
    search_fields = ('岗位',)
    # queryset 是默认的结果，search_term 是在后台搜索的关键词
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(ArticleAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct
admin.site.register(Data1,ArticleAdmin)
from .models import Search
admin.site.register(Search)


# -*- coding:utf-8 -*-
from django.contrib import admin

# Register your models here.
from myblog.models import Blog, Category, Tag

#admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)

#但是，我们点击进入我的博客后，发现只有博客的标题展示出来，如果我们还想添加其它字段，比如点击数、发表时间等，同样可以在admin.py中进行配置：
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'create_time', 'modify_time']

admin.site.register(Blog, BlogAdmin)

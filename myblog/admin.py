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

    def save_model(self, request, obj, form, change):
        obj.save()
        #博客分类数目统计
        obj_category = obj.category
        category_number = obj_category.blog_set.count()
        obj_category.number = category_number
        obj_category.save()
        #博客标签数目统计
        obj_tag_list = obj.tag.all()
        for obj_tag in obj_tag_list:
            tag_number = obj_tag.blog_set.count()
            obj_tag.number = tag_number
            obj_tag.save()

    def delete_model(self, request, obj, form, change):
        obj.delete()
        #博客分类数目统计
        obj_category = obj.category
        category_number = obj_category.blog_set.count()
        obj_category.number = category_number
        obj_category.save()
        #博客标签数目统计
        obj_tag_list = obj.tag.all()
        for obj_tag in obj_tag_list:
            tag_number = obj_tag.blog_set.count()
            obj_tag.number = tag_number
            obj_tag.save()


admin.site.register(Blog, BlogAdmin)

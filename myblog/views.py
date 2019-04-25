# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views import View
# Create your views here.


'''
class IndexView(View):
    """
    首页
    """
    def get(self, request):
        return render(request, 'index.html')
'''

from myblog.models import Blog, Category, Tag

class IndexView(View):
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        return render(request, 'index.html', {
            'all_blog': all_blog,
        })


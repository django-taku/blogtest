from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from. models import BlogModel
from django.urls import reverse_lazy

class BlogList(ListView): # データの一覧に適したもの
    template_name = 'list.html'
    model = BlogModel

class BlogDetail(DetailView):# データベースに入っている個別の記事に表示させる際に使う
    template_name = 'detail.html'
    model = BlogModel

class BlogCreate(CreateView):# ブラウザ上で入力データのやりとり
    template_name = 'create.html'
    model = BlogModel
    fields = ('title', 'content', 'category')# ブラウザ上で表示させる項目を指定
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list') # 一覧

# Create your views here.

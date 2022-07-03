from django.shortcuts import render
from blog.models import Blog
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    fields = ['title', 'subtitle', 'date', 'autor', 'body', 'photo']

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy('blog:blog-list')
    fields = ['title', 'subtitle', 'date', 'autor', 'body', 'photo']

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy('blog:blog-list')
    fields = ['title', 'subtitle', 'date', 'autor', 'body', 'photo']

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog-list')
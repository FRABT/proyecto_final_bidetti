from django.shortcuts import render
from comment.models import Comment
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CommentListView(ListView):
    model = Comment
    template_name = "comment/comment_list.html"

class CommentDetailView(DetailView):
    model = Comment
    template_name = "comment/comment_detail.html"
    fields = ['date', 'blog_title', 'comments']

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    success_url = reverse_lazy('comment:comment-list')
    fields = ['date', 'blog_title', 'comments']

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    success_url = reverse_lazy('comment:comment-list')
    fields = ['date', 'blog_title', 'comments']

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('comment:comment-list')
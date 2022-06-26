from django.urls import path
from blog import views


app_name='blog'

urlpatterns = [
    path('add/',views.blog_forms_view, name='BlogForm'),
    path('', views.BlogListView.as_view(), name='Blogs'),
    path('<int:pk>/detail', views.BlogDetailView.as_view(), name='blog-detail'),
]
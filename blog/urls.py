from django.urls import path
from blog import views


app_name='blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('add/', views.BlogCreateView.as_view(), name='blog-add'),
    path('<int:pk>/detail', views.BlogDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog-delete'),
]
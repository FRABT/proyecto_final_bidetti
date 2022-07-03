from django.urls import path
from comment import views

app_name='comment'

urlpatterns = [
    path('', views.CommentListView.as_view(), name='comment-list'),
    path('add/', views.CommentCreateView.as_view(), name='comment-add'),
    path('<int:pk>/detail', views.CommentDetailView.as_view(), name='comment-detail'),
    path('<int:pk>/update', views.CommentUpdateView.as_view(), name='comment-update'),
    path('<int:pk>/delete', views.CommentDeleteView.as_view(), name='comment-delete'),
]
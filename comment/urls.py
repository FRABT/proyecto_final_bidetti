from django.urls import path
from comment import views

app_name='comment'

urlpatterns = [
    path('', views.comment, name='Comments'),
    path('commentsform/',views.comment_forms_view, name='CommentForm'),
]
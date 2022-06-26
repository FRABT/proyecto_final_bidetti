from django.urls import path

from home import views

app_name='home'
urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
]
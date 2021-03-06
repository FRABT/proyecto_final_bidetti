from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views

app_name='home'
urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
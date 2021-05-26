from django.urls import path
from . import views
from .views import BlogView, ArticleDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blog', BlogView.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]
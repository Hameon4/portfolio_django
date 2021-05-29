from django.urls import path
from . import views
from .views import BlogView, ArticleDetailView, AddPostView, UpdatePostView

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blog', BlogView.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('blog/add_post/', AddPostView.as_view(), name='add_post'),
    path('blog/article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
]
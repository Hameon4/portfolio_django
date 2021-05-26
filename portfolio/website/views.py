from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import translation

from .models import Post, Category


class HomePageView(ListView):
    template_name = 'blog/index.html'
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(lang=translation.get_language(),
                                         status=Post.PUBLISHED)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return super().get_queryset().filter(lang=translation.get_language(),
                                             status=Post.PUBLISHED)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context['object']
        context['related_articles'] = Post.objects.\
            filter(status=Post.PUBLISHED,
                   lang=translation.get_language(),
                   category=article.category).\
            exclude(id=article.id)
        return context


class CategoryDetailView(DetailView):
    template_name = 'blog/category_detail.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(lang=translation.get_language(),
                                               status=Post.PUBLISHED)
        return context

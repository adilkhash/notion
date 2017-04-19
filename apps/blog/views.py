from django.views.generic import ListView, DetailView
from django.utils import translation

from .models import Post, Category, Page


class HomePageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(lang=translation.get_language(),
                                         status=Post.PUBLISHED).order_by('-id')


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return super().get_queryset().filter(lang=translation.get_language(),
                                             status=Post.PUBLISHED)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context['object']
        article.page_views += 1
        article.save()
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
                                               status=Post.PUBLISHED).order_by('-created')
        return context


class ArchiveListView(ListView):
    model = Post
    template_name = 'blog/archives.html'

    def get_queryset(self):
        return super().get_queryset().filter(lang=translation.get_language(),
                                             status=Post.PUBLISHED).order_by('category').\
            select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list_by_year'] = self.get_queryset().\
            filter(lang=translation.get_language(),
                   status=Post.PUBLISHED).order_by('-created')
        return context


class PageDetailView(DetailView):
    template_name = 'blog/page.html'
    model = Page

    def get_queryset(self):
        return super().get_queryset().filter(lang=translation.get_language(),
                                             visible=True)

from django.views.generic import ListView, DetailView, View
from django.utils import translation
from django.utils.translation import gettext as _
from django.urls import reverse, reverse_lazy
from django.contrib.syndication.views import Feed
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.db.models import F
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.shortcuts import render

from apps.blog.models import Post, Category, Page, EmailSubscription, AlternateURL
from apps.blog.forms import EmailForm


class LastestPostFeed(Feed):
    title = _("Adil Khashtamov's personal blog")
    description = _('pragmatic programmer')
    link = reverse_lazy('blog:posts')

    def items(self):
        return Post.objects.filter(
            lang=translation.get_language(), status=Post.PUBLISHED
        ).order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text[: item.text.find('<!--more-->')]

    def item_link(self, item):
        return reverse('blog:post', kwargs={'slug': item.slug})


class HomePageView(ListView):
    template_name = 'blog/index.html'
    model = Post

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.filter(lang=translation.get_language()).order_by(
                '-id'
            )
        else:
            return self.model.objects.filter(
                lang=translation.get_language(), status=Post.PUBLISHED
            ).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['popular_posts'] = self.model.objects.filter(
            lang=translation.get_language(), status=Post.PUBLISHED
        ).order_by('-page_views')[:10]
        context['recent_posts'] = self.model.objects.filter(
            lang=translation.get_language(), status=Post.PUBLISHED
        ).order_by('-id')[:10]
        return context


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        if self.request.user.is_superuser:
            return super().get_queryset().filter(lang=translation.get_language())
        else:
            return (
                super()
                .get_queryset()
                .filter(lang=translation.get_language(), status=Post.PUBLISHED)
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context['object']
        article.page_views = F('page_views') + 1
        article.save()
        context['object'] = self.model.objects.get(id=article.id)

        context['related_articles'] = Post.objects.filter(
            status=Post.PUBLISHED,
            lang=translation.get_language(),
            category=article.category,
        ).exclude(id=article.id)
        context['alternate_posts'] = AlternateURL.objects.filter(post=self.object)
        context['popular_posts'] = self.model.objects.filter(
            lang=translation.get_language(), status=Post.PUBLISHED
        ).order_by('-page_views')[:10]
        context['recent_posts'] = self.model.objects.filter(
            lang=translation.get_language(), status=Post.PUBLISHED
        ).order_by('-id')[:10]
        return context


class CategoryDetailView(DetailView):
    template_name = 'blog/category_detail.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(
            lang=translation.get_language(),
            status=Post.PUBLISHED,
            category=self.get_object(),
        ).order_by('-created')
        return context


class PageDetailView(DetailView):
    template_name = 'blog/page.html'
    model = Page

    def get_queryset(self):
        return (
            super().get_queryset().filter(lang=translation.get_language(), visible=True)
        )


class SearchView(View):
    def get(self, request):
        lang_mapping = {'en': 'english', 'ru': 'russian'}
        query = request.GET.get('query')
        lang = translation.get_language()
        lang_config = lang_mapping.get(lang, 'russian')
        search_query = SearchQuery(query, config=lang_config)
        vector = SearchVector('text', config=lang_config)
        results = (
            Post.objects.annotate(search=vector)
            .filter(lang=lang, search=search_query)
            .order_by('-created')
        )
        return render(request, 'blog/search.html', {'results': results, 'query': query})

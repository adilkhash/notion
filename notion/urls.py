from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from apps.blog.models import Post, Page
from apps.blog.views import SubscriptionView

blog_dict = {
    'queryset': Post.objects.filter(status=Post.PUBLISHED),
    'date_field': 'created',
}

page_dict = {
    'queryset': Page.objects.filter(visible=True),
    'date_field': 'created'
}

urlpatterns = [
    url(
        r'^sitemap\.xml$',
        sitemap, {
            'sitemaps': {
                'blog': GenericSitemap(blog_dict, priority=1),
                'page': GenericSitemap(page_dict, priority=0.5)
            }
        }, name='django.contrib.sitemaps.views.sitemap'
    ),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^courses/', include('apps.courses.urls'), name='courses'),
    url(r'^cpadmin/', admin.site.urls),
    url(r'^subscribe/$', SubscriptionView.as_view(), name='subscription'),
]

urlpatterns += i18n_patterns(
    url(r'^', include('apps.blog.urls', namespace='blog'))
)

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from apps.blog.models import Post, Page

blog_dict = {
    'queryset': Post.objects.filter(status=Post.PUBLISHED),
    'date_field': 'created',
}

page_dict = {
    'queryset': Page.objects.filter(visible=True),
    'date_field': 'created'
}

urlpatterns = [
    path(
        'robots.txt',
        TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),
        name='robots_txt'
    ),
    path(
        'sitemap.xml',
        sitemap, {
            'sitemaps': {
                'blog': GenericSitemap(blog_dict, priority=1, protocol='https'),
                'page': GenericSitemap(page_dict, priority=0.5, protocol='https')
            }
        }, name='django.contrib.sitemaps.views.sitemap'
    ),
    path('redactor/', include('redactor.urls')),
    path('cpadmin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('apps.blog.urls', namespace='blog')),
)

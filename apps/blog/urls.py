from django.conf.urls import url

from .views import (
    HomePageView, PostDetailView, CategoryDetailView, ArchiveListView,
    PageDetailView, LastestPostFeed, SearchView
)

app_name = 'blog'
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='posts'),
    url(r'^p/(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='page'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category'),
    url(r'^archives/$', ArchiveListView.as_view(), name='archives'),
    url(r'^feed/$', LastestPostFeed(), name='feed'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post'),
]

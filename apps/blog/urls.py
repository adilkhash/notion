from django.urls import path

from apps.blog.views import (
    HomePageView,
    PostDetailView,
    CategoryDetailView,
    ArchiveListView,
    PageDetailView,
    LastestPostFeed,
    SearchView,
)

app_name = 'blog'
urlpatterns = [
    path('', HomePageView.as_view(), name='posts'),
    path('p/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('^category/<slug:slug>/', CategoryDetailView.as_view(), name='category'),
    path('archives/', ArchiveListView.as_view(), name='archives'),
    path('feed/', LastestPostFeed(), name='feed'),
    path('search/', SearchView.as_view(), name='search'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post'),
]

from django.conf.urls import url

from .views import HomePageView, PostDetailView, CategoryDetailView, ArchiveListView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='posts'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category'),
    url(r'^archives/$', ArchiveListView.as_view(), name='archives'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post'),
]



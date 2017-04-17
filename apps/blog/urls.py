from django.conf.urls import url

from .views import HomePageView, PostDetailView, CategoryDetailView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='posts'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category'),
]

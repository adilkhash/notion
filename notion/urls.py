from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    url(r'^redactor/', include('redactor.urls')),
    url(r'^cpadmin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    url(r'^', include('apps.blog.urls', namespace='blog'))
)

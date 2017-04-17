from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=30)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title


class Post(models.Model):
    DRAFT, PUBLISHED = range(2)

    STATUSES = (
        (DRAFT, _('Draft')),
        (PUBLISHED, _('Published'))
    )

    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=100)
    text = models.TextField(_('Text'))
    lang = models.CharField(_('Language'), max_length=2, choices=settings.LANGUAGES)
    category = models.ForeignKey('Category', null=True)
    status = models.SmallIntegerField(_('Status'), choices=STATUSES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

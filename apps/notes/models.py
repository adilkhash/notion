from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse




class Theme(models.Model):
    title = models.CharField(_('Title'), max_length=30)
    slug = models.SlugField(_('Slug'), max_length=64)

    class Meta:
        verbose_name = _('theme')
        verbose_name_plural = _('Themes')

    def __str__(self):
        return self.title


class Note(models.Model):
    DRAFT, PUBLISHED = range(2)

    STATUSES = ((DRAFT, _('Draft')), (PUBLISHED, _('Published')))

    slug = models.SlugField(_('Slug'), max_length=100)
    title = models.CharField(_('Title'), max_length=254)
    text = models.TextField(_('Text'))
    created = models.DateTimeField(auto_now_add=True)
    lang = models.CharField(_('Language'), max_length=2, choices=settings.LANGUAGES)
    status = models.SmallIntegerField(_('Status'), choices=STATUSES)
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('note')
        verbose_name_plural = _('Notes')

    def get_absolute_url(self):
        return '/{}/{}/'.format(self.lang, self.slug)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse(
            'admin:%s_%s_change' % (content_type.app_label, content_type.model),
            args=(self.id,),
        )

    def __str__(self):
        return self.title

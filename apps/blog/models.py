import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType


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

    title = models.CharField(_('Title'), max_length=254)
    slug = models.SlugField(_('Slug'), max_length=100)
    text = models.TextField(_('Text'))
    lang = models.CharField(_('Language'), max_length=2, choices=settings.LANGUAGES)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)
    status = models.SmallIntegerField(_('Status'), choices=STATUSES)
    page_views = models.PositiveIntegerField(_('Page views'), default=0)
    featured_image = models.ImageField(
        _('Featured image'),
        upload_to='posts/',
        blank=True,
        null=True,
        help_text=_('Used for social sharing previews (recommended: 1200x630px)')
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/{}/{}/'.format(self.lang, self.slug)

    def month_year(self) -> str:
        return _(self.created.strftime('%B')) + ', ' + self.created.strftime('%Y')

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse('admin:%s_%s_change' % (content_type.app_label, content_type.model),
                       args=(self.id,))

    @property
    def is_draft(self):
        return self.status == self.DRAFT


class Page(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    text = models.TextField(_('Text'))
    lang = models.CharField(_('Language'), max_length=2, choices=settings.LANGUAGES)
    visible = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('Pages')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/{}/p/{}/'.format(self.lang, self.slug)


class EmailSubscription(models.Model):
    email = models.EmailField(_('Email'), unique=True)
    lang = models.CharField(_('Language'), max_length=2)
    activated = models.BooleanField(_('Activated'), default=False)
    activation_code = models.UUIDField(_('Activation code'), default=uuid.uuid4, editable=False)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('subscription')
        verbose_name_plural = _('Subscriptions')

    def __str__(self):
        return self.email

    def activate(self):
        self.activated = True
        self.save()

    def send_activation_code(self):
        pass


class AlternateURL(models.Model):
    post = models.ForeignKey('Post', verbose_name=_('Original post'), on_delete=models.CASCADE)
    lang = models.CharField(_('Language'), max_length=2, choices=settings.LANGUAGES)
    alternate_post = models.ForeignKey('Post', related_name='alternate_post',
                                       verbose_name=_('Alternate post'), on_delete=models.CASCADE)
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        verbose_name = _('alternate URL')
        verbose_name_plural = _('Alternate URLs')

    def __str__(self):
        return self.post.slug

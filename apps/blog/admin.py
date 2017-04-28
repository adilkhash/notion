from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor

from .models import Category, Post, Page, EmailSubscription


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'text', 'lang', 'status', 'category']
        widgets = {
           'text': RedactorEditor(redactor_options={
               'plugins': ['source'],
               'removeComments': False
           }),
        }


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'slug', 'text', 'lang', 'visible']
        widgets = {
           'text': RedactorEditor(redactor_options={'plugins': ['source']}),
        }


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created']
    search_fields = ['title']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'page_views', 'lang', 'slug', 'status', 'created']
    search_fields = ['title']
    ordering = ['-created']
    form = PostAdminForm


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'lang', 'slug', 'visible', 'created']
    form = PageAdminForm


class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'lang', 'created']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(EmailSubscription, EmailSubscriptionAdmin)

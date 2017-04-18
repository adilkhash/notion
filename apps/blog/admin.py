from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor

from .models import Category, Post, Page


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'text', 'lang', 'status', 'category']
        widgets = {
           'text': RedactorEditor(redactor_options={'plugins': ['source']}),
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
    list_display = ['title', 'lang', 'slug', 'status', 'created']
    search_fields = ['title']
    form = PostAdminForm


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'lang', 'slug', 'visible', 'created']
    form = PageAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

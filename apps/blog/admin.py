from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor

from .models import Category, Post


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'text', 'lang', 'status', 'category']
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


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

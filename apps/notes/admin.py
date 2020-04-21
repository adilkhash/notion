from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor

from apps.notes.models import Note, Theme


class NoteAdminForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'slug', 'text', 'lang', 'status', 'theme']
        widgets = {
           'text': RedactorEditor(redactor_options={
               'plugins': ['table'],

           }),
        }


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'lang', 'slug', 'status', 'created']
    search_fields = ['title']
    ordering = ['-created']
    form = NoteAdminForm


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title']


admin.site.register(Note, NoteAdmin)
admin.site.register(Theme, ThemeAdmin)

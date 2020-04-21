from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.utils import translation

from apps.notes.models import Note, Theme


class NotesListView(ListView):
    model = Note
    template_name = 'notes/notes.html'

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(lang=translation.get_language(), status=Note.PUBLISHED)
            .order_by('theme')
            .select_related('theme')
        )


class NoteDetailView(View):
    def get(self, request, theme_name: str, slug: str):
        theme = get_object_or_404(Theme, slug=theme_name)
        note = get_object_or_404(Note, slug=slug, status=Note.PUBLISHED)
        return render(request, 'notes/note_detail.html', {
            'theme': theme,
            'object': note
        })

from django.urls import path

from apps.notes.views import (
    NoteDetailView,
    NotesListView,
)

app_name = 'notes'
urlpatterns = [
    path('', NotesListView.as_view(), name='notes-list'),
    path('<slug:theme_name>/<slug:slug>/', NoteDetailView.as_view(), name='note-detail'),
]

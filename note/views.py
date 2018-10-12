from django.shortcuts import render

from .models import Note
from .forms import NoteForm

LIST_CHARS = [chr(char) for char in range(33, 65)] + \
             [chr(char) for char in range(91, 97)] + \
             [chr(char) for char in range(123, 128)]

def count_unique_words(note):
    text = note
    for char in LIST_CHARS:
        text = text.replace(char, '')
    text = text.lower()
    words = text.split()
    unique_words = []
    for word in words:
        if word in unique_words:
            pass
        else:
            unique_words.append(word)
    return len(unique_words)


def view_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.count_unique_words = count_unique_words(note.note)
            note.save()
    notes = Note.objects.all().order_by('count_unique_words')
    form = NoteForm()
    return render(request,
                  'note/index.html',
                  {'notes': notes,
                   'form': form})
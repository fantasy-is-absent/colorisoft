from django.shortcuts import render
from rest_framework import generics

from .models import Note
from .forms import NoteForm
from .serializers import NoteSerializer


class NoteViewSet(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('count_unique_words')
    serializer_class = NoteSerializer


def view_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
    notes = Note.objects.all().order_by('count_unique_words')
    form = NoteForm()
    return render(request,
                  'note/index.html',
                  {'notes': notes,
                   'form': form})
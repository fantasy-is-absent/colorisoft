from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note
        fields = ('note', 'count_unique_words')
        read_only_fields = ('count_unique_words',)

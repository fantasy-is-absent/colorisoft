from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('note', 'count_unique_words')
        read_only_fields = ('count_unique_words',)

    def create(self, validated_data):
        note = Note(note=validated_data['note'])
        note.save()
        return note

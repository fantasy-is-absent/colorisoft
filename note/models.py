from django.db import models

LIST_CHARS = [chr(char) for char in range(33, 65)] + \
             [chr(char) for char in range(91, 97)] + \
             [chr(char) for char in range(123, 128)]

class Note(models.Model):
    note = models.CharField(max_length=154,
                            blank=False,
                            null=False)
    count_unique_words = models.IntegerField(blank=True,
                                             null=True)

    def save(self):
        text = self.note
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
        self.count_unique_words = len(unique_words)
        super(Note, self).save()
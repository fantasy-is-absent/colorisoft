from django.db import models


class Note(models.Model):
    note = models.CharField(max_length=154,
                            blank=False,
                            null=False)
    count_unique_words = models.IntegerField(blank=False,
                            null=False)
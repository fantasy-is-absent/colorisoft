# Generated by Django 2.1.2 on 2018-10-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=154)),
                ('count_unique_words', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

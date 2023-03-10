# Generated by Django 4.1.4 on 2023-01-17 13:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_alter_mangapost_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MangaComment',
            fields=[
                ('body', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatroom.mangapost')),
            ],
        ),
    ]

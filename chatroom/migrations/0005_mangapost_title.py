# Generated by Django 4.1.4 on 2023-01-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0004_mangacomment_post_alter_mangacomment_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='mangapost',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

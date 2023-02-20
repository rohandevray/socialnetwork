# Generated by Django 4.1.4 on 2023-01-17 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_follower_follows_alter_follower_owner'),
        ('chatroom', '0003_mangacomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mangacomment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatroom.mangapost'),
        ),
        migrations.AlterField(
            model_name='mangacomment',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]

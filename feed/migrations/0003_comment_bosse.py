# Generated by Django 4.1.4 on 2023-01-16 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_follower_follows_alter_follower_owner'),
        ('feed', '0002_comment_owner_post_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='bosse',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-23 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_clone', '0003_remove_comment_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='totalViews',
        ),
        migrations.AddField(
            model_name='ytvideo',
            name='totalViews',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
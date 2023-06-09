# Generated by Django 4.1.5 on 2023-02-23 04:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='YTClient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstName', models.CharField(blank=True, max_length=100, null=True)),
                ('lastName', models.CharField(blank=True, max_length=100, null=True)),
                ('emailID', models.EmailField(blank=True, max_length=100, null=True)),
                ('subscription', models.BooleanField(default=False)),
                ('location', models.CharField(choices=[('IN', 'India'), ('AR', 'Argentina'), ('CA', 'Canada'), ('PR', 'Portugal')], default='IN', max_length=2)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='YTVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube_clone.ytclient')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(default='')),
                ('totalViews', models.PositiveIntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube_clone.ytclient')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='YTVideo', to='youtube_clone.ytvideo')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube_clone.ytclient')),
            ],
        ),
    ]

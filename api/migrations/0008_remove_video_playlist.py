# Generated by Django 4.0.2 on 2022-03-06 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_video_playlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='playlist',
        ),
    ]
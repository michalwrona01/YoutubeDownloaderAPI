# Generated by Django 4.0.2 on 2022-03-06 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_video_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='playlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.playlist'),
        ),
    ]

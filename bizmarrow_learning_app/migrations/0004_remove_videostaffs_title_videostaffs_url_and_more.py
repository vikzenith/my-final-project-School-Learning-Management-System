# Generated by Django 4.2.7 on 2023-12-15 04:50

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bizmarrow_learning_app', '0003_rename_video_url_videostaffs_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videostaffs',
            name='title',
        ),
        migrations.AddField(
            model_name='videostaffs',
            name='url',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
        migrations.AlterField(
            model_name='videostaffs',
            name='message',
            field=models.CharField(max_length=250, null=True),
        ),
    ]

# Generated by Django 2.0.7 on 2018-08-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0040_auto_20180819_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='button_color',
            field=models.CharField(default='ffffff', max_length=120),
        ),
        migrations.AddField(
            model_name='video',
            name='play_pause_active',
            field=models.BooleanField(default=True),
        ),
    ]

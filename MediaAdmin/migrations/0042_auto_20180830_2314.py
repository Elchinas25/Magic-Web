# Generated by Django 2.0.7 on 2018-08-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0041_auto_20180830_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='digonalstyle',
            name='second_sec_title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='second_sec_title_color',
            field=models.CharField(default='ffffff', max_length=120),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='third_sec_title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='third_sec_title_color',
            field=models.CharField(default='ffffff', max_length=120),
        ),
    ]

# Generated by Django 2.0.7 on 2018-08-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0008_auto_20180810_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallerystyleadmin',
            options={'verbose_name_plural': 'Gallery styles'},
        ),
        migrations.AddField(
            model_name='event',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='title_en',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='title_es',
            field=models.CharField(max_length=120, null=True),
        ),
    ]

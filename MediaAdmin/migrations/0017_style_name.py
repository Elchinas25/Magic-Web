# Generated by Django 2.0.7 on 2018-08-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0016_auto_20180802_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='name',
            field=models.CharField(default='MainStylesAdmin', max_length=120),
        ),
    ]

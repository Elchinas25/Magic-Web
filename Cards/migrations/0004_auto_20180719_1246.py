# Generated by Django 2.0.7 on 2018-07-19 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0003_auto_20180719_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercard',
            old_name='name',
            new_name='slug',
        ),
    ]

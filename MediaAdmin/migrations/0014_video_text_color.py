# Generated by Django 2.0.7 on 2018-08-01 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0013_auto_20180801_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='text_color',
            field=models.CharField(default='000000', help_text='Default = BLACK', max_length=120),
        ),
    ]

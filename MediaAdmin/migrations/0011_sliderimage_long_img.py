# Generated by Django 2.0.7 on 2018-07-30 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0010_auto_20180725_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='long_img',
            field=models.BooleanField(default=False),
        ),
    ]

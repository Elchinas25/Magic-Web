# Generated by Django 2.0.7 on 2018-09-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0046_auto_20180901_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='digonalstyle',
            name='fourth_sec_mob_height',
            field=models.IntegerField(default=300),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='second_sec_mob_height',
            field=models.IntegerField(default=300),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='third_sec_mob_height',
            field=models.IntegerField(default=300),
        ),
    ]
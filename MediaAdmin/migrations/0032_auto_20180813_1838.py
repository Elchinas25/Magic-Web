# Generated by Django 2.0.7 on 2018-08-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0031_auto_20180813_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='digonalstyle',
            name='statement_en',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='statement_es',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
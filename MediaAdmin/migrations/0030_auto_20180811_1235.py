# Generated by Django 2.0.7 on 2018-08-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0029_style_main_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='main_img_bg_color',
            field=models.CharField(default='000000', max_length=120),
        ),
        migrations.AddField(
            model_name='style',
            name='main_img_text_color',
            field=models.CharField(default='ffffff', max_length=120),
        ),
    ]
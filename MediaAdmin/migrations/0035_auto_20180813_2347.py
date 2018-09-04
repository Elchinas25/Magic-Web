# Generated by Django 2.0.7 on 2018-08-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0034_auto_20180813_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='digonalstyle',
            name='second_sec_bg_color',
            field=models.CharField(default='000000', max_length=120),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='second_sec_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='second_sec_text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='second_sec_text_en',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='second_sec_text_es',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='third_sec_bg_color',
            field=models.CharField(default='000000', max_length=120),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='third_sec_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='third_sec_text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='third_sec_text_en',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='digonalstyle',
            name='third_sec_text_es',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
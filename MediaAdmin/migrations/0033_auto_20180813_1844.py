# Generated by Django 2.0.7 on 2018-08-13 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0032_auto_20180813_1838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='style',
            options={'verbose_name_plural': 'Landing Page Admin'},
        ),
        migrations.RenameField(
            model_name='digonalstyle',
            old_name='main_img_text_color',
            new_name='statement_color',
        ),
    ]
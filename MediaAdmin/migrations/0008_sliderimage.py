# Generated by Django 2.0.7 on 2018-07-24 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MediaAdmin', '0007_auto_20180724_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('active', models.BooleanField()),
                ('img', models.ImageField(upload_to='images/')),
                ('text', models.CharField(blank=True, max_length=160, null=True)),
                ('show_text', models.BooleanField(default=False)),
                ('fkey', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='MediaAdmin.SliderAdmin')),
            ],
        ),
    ]

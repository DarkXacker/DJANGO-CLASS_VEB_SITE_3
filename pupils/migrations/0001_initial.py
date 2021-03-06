# Generated by Django 4.0.5 on 2022-06-09 03:12

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familya', models.CharField(max_length=100)),
                ('sharif', models.CharField(max_length=100)),
                ('tug_kun', models.DateField()),
                ('telefon', models.IntegerField()),
                ('haqida', ckeditor.fields.RichTextField()),
                ('rasmi', models.ImageField(blank=True, upload_to='pupils/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olimps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olimp',
            name='name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='olimp',
            name='videofile',
            field=models.FileField(blank=True, null=True, upload_to='videos/', verbose_name=''),
        ),
    ]

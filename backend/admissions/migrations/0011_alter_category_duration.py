# Generated by Django 5.0.4 on 2024-04-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0010_banner_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='duration',
            field=models.FloatField(default=0),
        ),
    ]

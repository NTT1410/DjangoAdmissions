# Generated by Django 5.0.4 on 2024-04-25 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0005_alter_school_description_alter_school_mission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='description',
            field=models.TextField(),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0014_delete_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]

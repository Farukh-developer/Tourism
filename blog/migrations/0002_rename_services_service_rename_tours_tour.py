# Generated by Django 5.0.6 on 2024-05-17 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.RenameModel(
            old_name='Tours',
            new_name='Tour',
        ),
    ]

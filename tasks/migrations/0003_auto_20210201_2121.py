# Generated by Django 3.1.6 on 2021-02-01 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20210201_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complet',
            new_name='complete',
        ),
    ]

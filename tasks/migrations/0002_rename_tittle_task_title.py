# Generated by Django 3.2.5 on 2021-09-27 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tittle',
            new_name='title',
        ),
    ]

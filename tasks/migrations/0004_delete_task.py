# Generated by Django 4.0.5 on 2022-06-22 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
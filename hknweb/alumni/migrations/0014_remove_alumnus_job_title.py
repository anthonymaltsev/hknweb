# Generated by Django 2.1.3 on 2018-11-10 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0013_remove_alumnus_nothing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnus',
            name='job_title',
        ),
    ]
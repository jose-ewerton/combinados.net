# Generated by Django 4.0 on 2022-10-29 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_combined_remove_task_description_remove_task_event_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
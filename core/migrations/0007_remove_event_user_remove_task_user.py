# Generated by Django 4.0 on 2022-10-25 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile_alter_event_user_alter_task_user_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]

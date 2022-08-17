# Generated by Django 4.0.5 on 2022-08-17 01:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Título do Evento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('1', 'ATIVIDADES'), ('2', 'DOAÇÕES')], max_length=100, verbose_name='Tipo de evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='tasks',
            field=models.CharField(max_length=100, verbose_name='Tarefa'),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user', verbose_name='Usuário'),
        ),
    ]
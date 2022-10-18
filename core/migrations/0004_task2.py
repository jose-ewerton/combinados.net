# Generated by Django 4.0.5 on 2022-08-17 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_event_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('description', models.TextField(verbose_name='Descrição da tarefa')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
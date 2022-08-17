# Generated by Django 4.0.5 on 2022-08-17 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('event_type', models.CharField(max_length=100, verbose_name='Tipo de evento')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('tasks', models.CharField(choices=[('1', 'ATIVIDADES'), ('2', 'DOAÇÕES')], max_length=100, verbose_name='Tipo de atividade')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('password', models.CharField(max_length=20, verbose_name='Senha')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
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
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-09-15 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('data_matricula', models.DateField(auto_now=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='escola.curso')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudante', to='escola.estudante')),
            ],
        ),
    ]

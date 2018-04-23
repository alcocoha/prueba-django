# Generated by Django 2.0.4 on 2018-04-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(choices=[('BUENO', 'Bueno'), ('MALO', 'Malo'), ('REGULAR', 'Regular')], default='BUENO', max_length=7)),
                ('id_pregunta', models.IntegerField()),
                ('id_usuario', models.IntegerField()),
            ],
        ),
    ]
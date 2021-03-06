# Generated by Django 4.0.1 on 2022-02-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255)),
                ('sobrenome', models.CharField(blank=True, max_length=255)),
                ('cpf', models.CharField(blank=True, max_length=14)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('celular', models.CharField(blank=True, max_length=255)),
                ('rua', models.CharField(blank=True, max_length=255)),
                ('numero', models.IntegerField(blank=True, max_length=255)),
                ('bairro', models.CharField(blank=True, max_length=255)),
                ('cidade', models.CharField(blank=True, max_length=255)),
                ('cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

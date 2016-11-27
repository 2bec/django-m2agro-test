# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('safras', '__first__'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=180)),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data_compra', models.DateTimeField(blank=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.Servico')),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='produtos',
            field=models.ManyToManyField(through='servicos.Valores', to='produtos.Produto'),
        ),
        migrations.AddField(
            model_name='servico',
            name='safra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safras.Safra'),
        ),
    ]

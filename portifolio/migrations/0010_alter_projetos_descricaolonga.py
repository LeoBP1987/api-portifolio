# Generated by Django 5.1.7 on 2025-03-28 19:58

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0009_alter_projetos_descricaobackend_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='descricaoLonga',
            field=markdownx.models.MarkdownxField(max_length=600),
        ),
    ]

# Generated by Django 5.1.4 on 2025-01-21 02:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.answer', verbose_name='답변'),
        ),
    ]

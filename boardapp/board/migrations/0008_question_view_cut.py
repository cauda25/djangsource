# Generated by Django 5.1.4 on 2025-01-22 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_answer_view_cut'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view_cut',
            field=models.IntegerField(default=0),
        ),
    ]

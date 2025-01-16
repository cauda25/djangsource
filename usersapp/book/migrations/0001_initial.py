# Generated by Django 5.1.4 on 2025-01-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='도서코드')),
                ('title', models.CharField(max_length=200, verbose_name='도서명')),
                ('author', models.CharField(max_length=100, verbose_name='저자')),
                ('price', models.IntegerField(verbose_name='도서가격')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='등록일시')),
            ],
            options={
                'db_table': 'booktbl',
            },
        ),
    ]

# Generated by Django 5.1.4 on 2025-01-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

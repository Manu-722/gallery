# Generated by Django 5.2.4 on 2025-07-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_photo_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

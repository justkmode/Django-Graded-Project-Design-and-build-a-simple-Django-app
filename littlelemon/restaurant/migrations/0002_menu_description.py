# Generated by Django 5.1.1 on 2024-10-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.TextField(default='No description available.'),
            preserve_default=False,
        ),
    ]

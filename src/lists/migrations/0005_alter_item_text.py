# Generated by Django 4.2.11 on 2024-04-05 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='', unique=True),
        ),
    ]

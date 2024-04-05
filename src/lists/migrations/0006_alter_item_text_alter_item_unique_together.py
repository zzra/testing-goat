# Generated by Django 4.2.11 on 2024-04-05 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]

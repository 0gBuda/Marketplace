# Generated by Django 5.0.3 on 2024-05-22 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_alter_products_name_alter_products_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='slug',
        ),
    ]

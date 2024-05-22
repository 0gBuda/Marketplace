# Generated by Django 5.0.3 on 2024-05-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_products_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, default=models.CharField(max_length=150), max_length=200, null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='firm',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

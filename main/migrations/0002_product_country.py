# Generated by Django 4.2.7 on 2023-11-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(default=0, max_length=255),
        ),
    ]

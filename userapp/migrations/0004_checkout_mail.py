# Generated by Django 4.2.7 on 2024-05-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_cartdb_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='mail',
            field=models.EmailField(default='null', max_length=254),
        ),
    ]

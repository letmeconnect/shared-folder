# Generated by Django 3.1.5 on 2021-06-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0016_auto_20210622_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_products',
            name='order_id',
            field=models.IntegerField(null=True),
        ),
    ]

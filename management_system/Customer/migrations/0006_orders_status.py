# Generated by Django 3.1.5 on 2021-05-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0005_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

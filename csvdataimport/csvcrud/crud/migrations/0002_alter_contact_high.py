# Generated by Django 4.0.2 on 2022-03-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='high',
            field=models.CharField(max_length=100),
        ),
    ]

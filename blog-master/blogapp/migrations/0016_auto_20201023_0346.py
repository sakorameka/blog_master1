# Generated by Django 3.0.7 on 2020-10-22 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_auto_20201023_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='text',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]
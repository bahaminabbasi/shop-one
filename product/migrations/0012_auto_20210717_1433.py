# Generated by Django 3.2.4 on 2021-07-17 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20210717_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=models.TextField(default='test'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specs',
            field=models.TextField(default='test'),
        ),
    ]
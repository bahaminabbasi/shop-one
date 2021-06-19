# Generated by Django 3.2.4 on 2021-06-19 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210616_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='nesting_level',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category'),
        ),
    ]

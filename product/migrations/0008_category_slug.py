# Generated by Django 3.2.4 on 2021-06-19 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_category_nesting_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, null=True),
        ),
    ]
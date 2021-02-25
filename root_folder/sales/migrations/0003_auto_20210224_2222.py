# Generated by Django 3.1.5 on 2021-02-24 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20210224_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='unit_sold2',
            field=models.DecimalField(decimal_places=0, help_text='max_digits = 9', max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='unit_sold3',
            field=models.DecimalField(decimal_places=0, help_text='max_digits = 9', max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
# Generated by Django 3.2.25 on 2024-07-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20240704_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='from_height',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='from_weight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='max_income',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='min_income',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='to_height',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='to_weight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

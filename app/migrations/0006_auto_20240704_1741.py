# Generated by Django 3.2.25 on 2024-07-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20240704_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='from_age',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='from_height',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='from_weight',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='max_income',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='min_income',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='to_age',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='to_height',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='to_weight',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
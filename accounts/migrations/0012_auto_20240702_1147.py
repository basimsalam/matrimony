# Generated by Django 3.2.25 on 2024-07-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_user_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address_line1',
            field=models.TextField(blank=True, max_length=100, verbose_name='Address Line1'),
        ),
        migrations.AddField(
            model_name='user',
            name='address_line2',
            field=models.TextField(blank=True, max_length=100, verbose_name='Address Line2'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, max_length=100, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='user',
            name='zipcode',
            field=models.CharField(blank=True, max_length=6, verbose_name='Zip Code'),
        ),
    ]
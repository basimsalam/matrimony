# Generated by Django 3.2.25 on 2024-07-04 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_partner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='caste',
            new_name='caste_p',
        ),
        migrations.RenameField(
            model_name='partner',
            old_name='religion',
            new_name='religion_p',
        ),
    ]
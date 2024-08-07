# Generated by Django 3.2.25 on 2024-07-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('unread', 'Unread'), ('delivered', 'Delivered'), ('read', 'Read')], default='unread', max_length=20, verbose_name='Status'),
        ),
    ]

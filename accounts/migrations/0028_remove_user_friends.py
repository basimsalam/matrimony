# Generated by Django 3.2.25 on 2024-07-12 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_rename_friend_request_friendrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
    ]

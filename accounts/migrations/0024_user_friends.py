# Generated by Django 3.2.25 on 2024-07-09 10:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_accounts_user_friends_+', to=settings.AUTH_USER_MODEL),
        ),
    ]

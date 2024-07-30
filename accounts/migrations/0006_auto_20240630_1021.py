# Generated by Django 3.2.25 on 2024-06-30 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_employementdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='drinking_habits',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='hobbies',
            field=models.ManyToManyField(blank=True, related_name='users', to='accounts.Hobby'),
        ),
        migrations.AlterField(
            model_name='user',
            name='smoking_habits',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=50),
        ),
    ]

# Generated by Django 3.2.25 on 2024-07-03 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Caste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(blank=True, max_length=100, verbose_name='Father Name')),
                ('father_occupation', models.CharField(blank=True, max_length=100, verbose_name='Father Occupation')),
                ('mother_name', models.CharField(blank=True, max_length=100, verbose_name='Mother Name')),
                ('mother_occupation', models.CharField(blank=True, max_length=100, verbose_name='Mother Occupation')),
                ('num_of_siblings', models.IntegerField(blank=True, verbose_name='Number Of Siblings')),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced')], max_length=100, verbose_name='Marital Status')),
                ('family_values', models.CharField(blank=True, choices=[('Orthodox', 'Orthodox'), ('Traditional', 'Traditional'), ('Moderate', 'Moderate'), ('Liberal', 'Liberal')], max_length=100)),
                ('disability', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=50, null=True)),
                ('family_type', models.CharField(blank=True, choices=[('Joint', 'Joint'), ('Nuclear', 'Nuclear')], max_length=50, null=True)),
                ('family_class', models.CharField(choices=[('Lower CLass', 'Lower CLass'), ('Middle Class', 'Middle Class'), ('Upper Class', 'Upper Class')], max_length=100)),
                ('caste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.caste')),
                ('religion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.religion')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

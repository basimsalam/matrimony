# Generated by Django 3.2.25 on 2024-07-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20240702_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employementdetails',
            name='is_employed',
        ),
        migrations.RemoveField(
            model_name='employementdetails',
            name='is_employer',
        ),
        migrations.RemoveField(
            model_name='employementdetails',
            name='is_job_seeker',
        ),
        migrations.AddField(
            model_name='employementdetails',
            name='job_status',
            field=models.CharField(blank=True, choices=[('Employee', 'Employee'), ('Employer', 'Employer'), ('Job Seeker', 'Job Seeker')], max_length=100, verbose_name='Job Status'),
        ),
        migrations.AlterField(
            model_name='employementdetails',
            name='company_location',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Company Location'),
        ),
        migrations.AlterField(
            model_name='employementdetails',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='employementdetails',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Designation'),
        ),
        migrations.AlterField(
            model_name='employementdetails',
            name='job_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Job Title'),
        ),
        migrations.AlterField(
            model_name='employementdetails',
            name='seeking_job_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Seeking Job Title'),
        ),
    ]
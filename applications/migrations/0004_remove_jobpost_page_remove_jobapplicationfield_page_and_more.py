# Generated by Django 5.1.7 on 2025-03-26 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_jobdetailpage_thank_you_text_jobapplicationfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='page',
        ),
        migrations.RemoveField(
            model_name='jobapplicationfield',
            name='page',
        ),
        migrations.RemoveField(
            model_name='jobdetailpage',
            name='job',
        ),
        migrations.RemoveField(
            model_name='jobdetailpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='CareersPage',
        ),
        migrations.DeleteModel(
            name='JobApplicationField',
        ),
        migrations.DeleteModel(
            name='JobPost',
        ),
        migrations.DeleteModel(
            name='JobDetailPage',
        ),
    ]

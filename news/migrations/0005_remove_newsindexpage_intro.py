# Generated by Django 5.1.7 on 2025-03-14 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_author_newsarticlepage_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsindexpage',
            name='intro',
        ),
    ]

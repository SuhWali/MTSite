# Generated by Django 5.1.7 on 2025-04-08 17:55

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0007_remove_applicationtrackingpage_page_ptr_and_more'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationTrackingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True, help_text='Introduction text for the application page')),
                ('deadline', models.DateTimeField(blank=True, help_text='Application deadline', null=True)),
                ('carousel_title_1', models.CharField(blank=True, max_length=100)),
                ('carousel_text_1', models.TextField(blank=True)),
                ('carousel_title_2', models.CharField(blank=True, max_length=100)),
                ('carousel_text_2', models.TextField(blank=True)),
                ('carousel_title_3', models.CharField(blank=True, max_length=100)),
                ('carousel_text_3', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Application Tracking Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ApplicationFormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='applications.applicationtrackingpage')),
            ],
            options={
                'verbose_name': 'Form Field',
                'verbose_name_plural': 'Form Fields',
                'ordering': ['sort_order'],
            },
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-26 09:16

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('header', wagtail.fields.StreamField([('header', 12)], blank=True, block_lookup={0: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 1: ('wagtail.blocks.CharBlock', (), {'required': False}), 2: ('wagtail.blocks.TextBlock', (), {'required': False}), 3: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('none', 'No Link'), ('page', 'Internal Page'), ('external', 'External URL')], 'help_text': 'Select the type of link you want to add'}), 4: ('wagtail.blocks.PageChooserBlock', (), {'help_text': 'Select an internal page to link to', 'required': False}), 5: ('wagtail.blocks.URLBlock', (), {'help_text': 'Enter an external URL to link to', 'required': False}), 6: ('wagtail.blocks.CharBlock', (), {'default': 'Read more', 'help_text': 'Text to display on the link button', 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('image', 0), ('title', 1), ('text', 2), ('link_type', 3), ('page_link', 4), ('external_link', 5), ('link_text', 6)]], {}), 8: ('wagtail.blocks.ListBlock', (7,), {}), 9: ('wagtail.blocks.BooleanBlock', (), {'default': True, 'help_text': 'Auto-rotate the carousel items', 'required': False}), 10: ('wagtail.blocks.BooleanBlock', (), {'default': True, 'help_text': 'Show the carousel indicators', 'required': False}), 11: ('wagtail.blocks.BooleanBlock', (), {'default': True, 'help_text': 'Show the carousel navigation arrows', 'required': False}), 12: ('wagtail.blocks.StructBlock', [[('items', 8), ('auto_play', 9), ('show_indicators', 10), ('show_arrows', 11)]], {})}, null=True)),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('full-time', 'Full Time'), ('part-time', 'Part Time'), ('internship', 'Internship'), ('contract', 'Contract')], max_length=50)),
                ('location', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('closing_date', models.DateField(blank=True, null=True)),
                ('description', wagtail.fields.RichTextField()),
                ('requirements', wagtail.fields.RichTextField()),
                ('responsibilities', wagtail.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('application_form_title', models.CharField(default='Apply Now', max_length=255)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.jobpost')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

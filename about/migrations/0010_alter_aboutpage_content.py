# Generated by Django 5.1.7 on 2025-03-26 04:05

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_alter_aboutpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='content',
            field=wagtail.fields.StreamField([('carousel', 12), ('mission_vision', 18), ('team_members', 27), ('cards', 33), ('heading', 35), ('call_to_action', 39)], blank=True, block_lookup={0: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 1: ('wagtail.blocks.CharBlock', (), {'required': False}), 2: ('wagtail.blocks.TextBlock', (), {'required': False}), 3: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('none', 'No Link'), ('page', 'Internal Page'), ('external', 'External URL')], 'help_text': 'Select the type of link you want to add'}), 4: ('wagtail.blocks.PageChooserBlock', (), {'help_text': 'Select an internal page to link to', 'required': False}), 5: ('wagtail.blocks.URLBlock', (), {'help_text': 'Enter an external URL to link to', 'required': False}), 6: ('wagtail.blocks.CharBlock', (), {'default': 'Read more', 'help_text': 'Text to display on the link button', 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('image', 0), ('title', 1), ('text', 2), ('link_type', 3), ('page_link', 4), ('external_link', 5), ('link_text', 6)]], {}), 8: ('wagtail.blocks.ListBlock', (7,), {}), 9: ('wagtail.blocks.BooleanBlock', (), {'default': True, 'help_text': 'Auto-rotate the carousel items', 'required': False}), 10: ('wagtail.blocks.BooleanBlock', (), {'default': True, 'help_text': 'Show the carousel indicators', 'required': False}), 11: ('wagtail.blocks.BooleanBlock', (), {'default': True, 'help_text': 'Show the carousel navigation arrows', 'required': False}), 12: ('wagtail.blocks.StructBlock', [[('items', 8), ('auto_play', 9), ('show_indicators', 10), ('show_arrows', 11)]], {}), 13: ('wagtail.blocks.TextBlock', (), {}), 14: ('wagtail.blocks.DateTimeBlock', (), {'format': '%Y-%m-%d', 'help_text': 'For timeline entries only', 'required': False}), 15: ('wagtail.blocks.PageChooserBlock', (), {'help_text': "Choose a page to link to for 'Learn More'", 'required': False}), 16: ('wagtail.blocks.StructBlock', [[('title', 1), ('content', 13), ('date', 14), ('learn_more', 15)]], {}), 17: ('wagtail.blocks.ListBlock', (16,), {}), 18: ('wagtail.blocks.StructBlock', [[('statement_items', 17)]], {}), 19: ('wagtail.blocks.CharBlock', (), {'default': 'Meet the Team', 'required': False}), 20: ('wagtail.blocks.CharBlock', (), {'required': True}), 21: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 22: ('wagtail.blocks.URLBlock', (), {'help_text': 'Facebook profile link', 'required': False}), 23: ('wagtail.blocks.URLBlock', (), {'help_text': 'Instagram profile link', 'required': False}), 24: ('wagtail.blocks.URLBlock', (), {'help_text': 'Twitter profile link', 'required': False}), 25: ('wagtail.blocks.StructBlock', [[('name', 20), ('role', 20), ('image', 0), ('bio', 21), ('facebook_link', 22), ('instagram_link', 23), ('twitter_link', 24)]], {}), 26: ('wagtail.blocks.ListBlock', (25,), {}), 27: ('wagtail.blocks.StructBlock', [[('title', 19), ('team_members', 26)]], {}), 28: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 29: ('wagtail.blocks.URLBlock', (), {'required': False}), 30: ('wagtail.blocks.CharBlock', (), {'default': 'Learn More', 'required': False}), 31: ('wagtail.blocks.StructBlock', [[('title', 20), ('image', 28), ('text', 21), ('link', 29), ('link_text', 30)]], {}), 32: ('wagtail.blocks.ListBlock', (31,), {}), 33: ('wagtail.blocks.StructBlock', [[('cards', 32)]], {}), 34: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')]}), 35: ('wagtail.blocks.StructBlock', [[('heading', 20), ('size', 34)]], {}), 36: ('wagtail.blocks.CharBlock', (), {'default': 'Learn More', 'required': True}), 37: ('wagtail.blocks.URLBlock', (), {'required': True}), 38: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('light', 'Light'), ('dark', 'Dark'), ('primary', 'Primary')]}), 39: ('wagtail.blocks.StructBlock', [[('title', 20), ('text', 21), ('button_text', 36), ('button_link', 37), ('background_color', 38)]], {})}),
        ),
    ]

# Generated by Django 5.1.7 on 2025-04-08 14:59

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_alter_newsarticlepage_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticlepage',
            name='body2',
            field=wagtail.fields.StreamField([('heading', 2), ('paragraph', 3), ('quote', 6), ('cta', 11), ('accordion', 15), ('two_column', 26)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')]}), 2: ('wagtail.blocks.StructBlock', [[('heading', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow'}), 4: ('wagtail.blocks.TextBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('quote', 4), ('attribution', 5)]], {}), 7: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 8: ('wagtail.blocks.CharBlock', (), {'default': 'Learn More', 'required': True}), 9: ('wagtail.blocks.URLBlock', (), {'required': True}), 10: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('light', 'Light'), ('dark', 'Dark'), ('primary', 'Primary')]}), 11: ('wagtail.blocks.StructBlock', [[('title', 0), ('text', 7), ('button_text', 8), ('button_link', 9), ('background_color', 10)]], {}), 12: ('wagtail.blocks.RichTextBlock', (), {'required': True}), 13: ('wagtail.blocks.StructBlock', [[('title', 0), ('content', 12)]], {}), 14: ('wagtail.blocks.ListBlock', (13,), {}), 15: ('wagtail.blocks.StructBlock', [[('items', 14)]], {}), 16: ('wagtail.blocks.RichTextBlock', (), {}), 17: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 18: ('wagtail.blocks.CharBlock', (), {'help_text': 'Alternative text for screen readers', 'required': False}), 19: ('wagtail.blocks.URLBlock', (), {'required': False}), 20: ('wagtail.blocks.StructBlock', [[('image', 17), ('caption', 5), ('alt_text', 18), ('link', 19)]], {}), 21: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('primary', 'Primary'), ('secondary', 'Secondary'), ('tertiary', 'Tertiary')]}), 22: ('wagtail.blocks.StructBlock', [[('text', 0), ('link', 9), ('style', 21)]], {}), 23: ('wagtail.blocks.StreamBlock', [[('heading', 2), ('paragraph', 16), ('image', 20), ('button', 22)]], {'icon': 'arrow-left', 'label': 'Left column content'}), 24: ('wagtail.blocks.StreamBlock', [[('heading', 2), ('paragraph', 16), ('image', 20), ('button', 22)]], {'icon': 'arrow-right', 'label': 'Right column content'}), 25: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('50-50', '50% / 50%'), ('33-67', '33% / 67%'), ('67-33', '67% / 33%')], 'help_text': 'Choose the width distribution of the columns'}), 26: ('wagtail.blocks.StructBlock', [[('left_column', 23), ('right_column', 24), ('column_distribution', 25)]], {})}, null=True),
        ),
    ]

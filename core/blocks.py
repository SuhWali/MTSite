from django import forms
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class HeadingBlock(blocks.StructBlock):
    """A heading with size options"""
    heading = blocks.CharBlock(required=True)
    size = blocks.ChoiceBlock(
        choices=[
            ('h2', 'H2'),
            ('h3', 'H3'),
            ('h4', 'H4'),
            ('h5', 'H5'),
            ('h6', 'H6'),
        ],
        default='h2',
    )

    class Meta:
        icon = 'title'
        template = 'blocks/heading_block.html'


class ImageBlock(blocks.StructBlock):
    """Image with caption and optional link"""
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)
    alt_text = blocks.CharBlock(required=False, help_text="Alternative text for screen readers")
    link = blocks.URLBlock(required=False)

    class Meta:
        icon = 'image'
        template = 'blocks/image_block.html'


class QuoteBlock(blocks.StructBlock):
    """Quote with attribution"""
    quote = blocks.TextBlock(required=True)
    attribution = blocks.CharBlock(required=False)

    class Meta:
        icon = 'openquote'
        template = 'blocks/quote_block.html'


class ButtonBlock(blocks.StructBlock):
    """Button with link and style options"""
    text = blocks.CharBlock(required=True)
    link = blocks.URLBlock(required=True)
    style = blocks.ChoiceBlock(
        choices=[
            ('primary', 'Primary'),
            ('secondary', 'Secondary'),
            ('tertiary', 'Tertiary'),
        ],
        default='primary',
    )

    class Meta:
        icon = 'link'
        template = 'blocks/button_block.html'


class CardBlock(blocks.StructBlock):
    """Card with image, title, text and link"""
    title = blocks.CharBlock(required=True)
    image = ImageChooserBlock(required=False)
    text = blocks.RichTextBlock(required=False)
    link = blocks.URLBlock(required=False)
    link_text = blocks.CharBlock(required=False, default="Read more")

    class Meta:
        icon = 'form'
        template = 'blocks/card_block.html'


class VideoBlock(blocks.StructBlock):
    """Embedded video with caption"""
    video = EmbedBlock(required=True)
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = 'media'
        template = 'blocks/video_block.html'


class DocumentBlock(blocks.StructBlock):
    """Document with title and description"""
    document = DocumentChooserBlock(required=True)
    title = blocks.CharBlock(required=False)
    description = blocks.TextBlock(required=False)

    class Meta:
        icon = 'doc-full'
        template = 'blocks/document_block.html'


class CallToActionBlock(blocks.StructBlock):
    """Call to action with title, text and button"""
    title = blocks.CharBlock(required=True)
    text = blocks.RichTextBlock(required=False)
    button_text = blocks.CharBlock(required=True, default="Learn More")
    button_link = blocks.URLBlock(required=True)
    background_color = blocks.ChoiceBlock(
        choices=[
            ('light', 'Light'),
            ('dark', 'Dark'),
            ('primary', 'Primary'),
        ],
        default='light',
    )

    class Meta:
        icon = 'pick'
        template = 'blocks/cta_block.html'


class AccordionItemBlock(blocks.StructBlock):
    """Single accordion item"""
    title = blocks.CharBlock(required=True)
    content = blocks.RichTextBlock(required=True)


class AccordionBlock(blocks.StructBlock):
    """Accordion with multiple expandable items"""
    items = blocks.ListBlock(AccordionItemBlock())

    class Meta:
        icon = 'list-ul'
        template = 'blocks/accordion_block.html'




class IconTextBlock(blocks.StructBlock):
    """Icon with text"""
    icon = blocks.CharBlock(required=True, help_text="Font Awesome icon name (e.g. 'fa-home')")
    title = blocks.CharBlock(required=True)
    text = blocks.TextBlock(required=False)

    class Meta:
        icon = 'placeholder'
        template = 'blocks/icon_text_block.html'


class TwoColumnBlock(blocks.StructBlock):
    """Two column layout with customizable widths"""
    left_column = blocks.StreamBlock([
        ('heading', HeadingBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageBlock()),
        ('button', ButtonBlock()),
    ], icon='arrow-left', label='Left column content')
    
    right_column = blocks.StreamBlock([
        ('heading', HeadingBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageBlock()),
        ('button', ButtonBlock()),
    ], icon='arrow-right', label='Right column content')
    
    column_distribution = blocks.ChoiceBlock(
        choices=[
            ('50-50', '50% / 50%'),
            ('33-67', '33% / 67%'),
            ('67-33', '67% / 33%'),
        ],
        default='50-50',
        help_text='Choose the width distribution of the columns'
    )

    class Meta:
        icon = 'grip'
        template = 'blocks/two_column_block.html'


class CarouselBlock(blocks.StructBlock):
    """Image carousel"""
    items = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock(required=True)),
            ('title', blocks.CharBlock(required=False)),
            ('text', blocks.TextBlock(required=False)),
            ('link', blocks.URLBlock(required=False)),
            ('link_text', blocks.CharBlock(required=False)),
        ])
    )

    class Meta:
        icon = 'image'
        template = 'blocks/carousel_block.html'


# Main StreamField block for use in page models
class BaseStreamBlock(blocks.StreamBlock):
    """
    Main streamfield block to be inherited by page models
    """
    heading = HeadingBlock()
    paragraph = blocks.RichTextBlock(icon='pilcrow')
    image = ImageBlock()
    quote = QuoteBlock()
    button = ButtonBlock()
    video = VideoBlock()
    document = DocumentBlock()
    cta = CallToActionBlock()
    accordion = AccordionBlock()
 
    two_column = TwoColumnBlock()
    carousel = CarouselBlock()
    embed = EmbedBlock(icon='media')
    
    class Meta:
        icon = 'placeholder'

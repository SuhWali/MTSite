from django import forms
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.blocks import PageChooserBlock

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
    """Image carousel with flexible link options"""
    items = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock(required=True)),
            ('title', blocks.CharBlock(required=False)),
            ('text', blocks.TextBlock(required=False)),
            ('link_type', blocks.ChoiceBlock(
                choices=[
                    ('none', 'No Link'),
                    ('page', 'Internal Page'),
                    ('external', 'External URL'),
                ],
                default='none',
                help_text='Select the type of link you want to add'
            )),
            ('page_link', PageChooserBlock(required=False, help_text='Select an internal page to link to')),
            ('external_link', blocks.URLBlock(required=False, help_text='Enter an external URL to link to')),
            ('link_text', blocks.CharBlock(required=False, default='Read more', help_text='Text to display on the link button')),
        ])
    )
    
    auto_play = blocks.BooleanBlock(required=False, default=True, help_text='Auto-rotate the carousel items')
    show_indicators = blocks.BooleanBlock(required=False, default=True, help_text='Show the carousel indicators')
    show_arrows = blocks.BooleanBlock(required=False, default=True, help_text='Show the carousel navigation arrows')
    
 
    
    class Meta:
        icon = 'image'
        template = 'blocks/home_carousel_block.html'
        

class SubscribeBlock(blocks.StructBlock):
    """Email subscription form with title and description"""
    title = blocks.CharBlock(required=False, default="Subscribe to our newsletter")
    description = blocks.TextBlock(required=False, default="Stay updated with our latest news and updates.")
    placeholder_text = blocks.CharBlock(required=False, default="Your email address")
    button_text = blocks.CharBlock(required=False, default="Subscribe")
    success_message = blocks.CharBlock(required=False, default="Thank you for subscribing!")
    background_color = blocks.ChoiceBlock(
        choices=[
            ('light', 'Light'),
            ('dark', 'Dark'),
            ('primary', 'Primary'),
        ],
        default='light',
    )

    class Meta:
        icon = 'mail'
        template = 'blocks/subscribe_block.html'


class TopArticlesBlock(blocks.StructBlock):
    """Block that displays the top articles"""
    title = blocks.CharBlock(required=False, default="Top Articles")
    number_of_articles = blocks.IntegerBlock(required=False, default=4, min_value=1, max_value=10, 
                                            help_text="Choose how many articles to display")
    show_images = blocks.BooleanBlock(required=False, default=True, 
                                     help_text="Show or hide the article featured images")
    show_date = blocks.BooleanBlock(required=False, default=True,
                                   help_text="Show or hide the article dates")
    show_author = blocks.BooleanBlock(required=False, default=False,
                                     help_text="Show or hide the article authors")
    
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        
        # Import here to avoid circular imports
        from news.models import NewsArticlePage
        from wagtail.models import Site
        
        # Get the current page from the parent context
        current_page = parent_context.get('page') if parent_context else None
        
        if current_page:
            # Get the current site
            current_site = Site.find_for_request(parent_context.get('request'))
            
            # Get the top articles ordered by date, filtered by the current site
            articles = NewsArticlePage.objects.live().filter(
                path__startswith=current_site.root_page.path
            ).order_by('-date')[:10]  # Fetch a few extra
        else:
            # Fallback if we can't determine the current site
            articles = NewsArticlePage.objects.live().order_by('-date')[:10]
        
        context['articles'] = articles
        return context
    
    class Meta:
        icon = 'list-ul'
        template = 'blocks/top_articles_block.html'
        label = 'Top Articles'





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
    subscribe = SubscribeBlock()
    top_articles = TopArticlesBlock()
 
    two_column = TwoColumnBlock()
    carousel = CarouselBlock()
    embed = EmbedBlock(icon='media')
    
    class Meta:
        icon = 'placeholder'



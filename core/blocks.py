from django import forms
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.blocks import PageChooserBlock

from wagtail.blocks import (
    StructBlock, CharBlock, TextBlock, 
    DateTimeBlock, ListBlock, StreamBlock
)

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
    """Group of cards displayed in a row"""
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ('title', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
            ('link', blocks.URLBlock(required=False)),
            ('link_text', blocks.CharBlock(required=False, default="Learn More")),
        ])
    )

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
        template = 'blocks/hero_carousel_block.html'
    
    def get_template(self, context):
        if context.get('template'):
            return context['template']
        return 'blocks/hero_carousel_block.html'
        

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
    view_all_link = blocks.URLBlock(required=False,
                                   help_text="Link to the articles listing page")
    
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
            ).order_by('-date')[:7]  # Fetch a few extra
        else:
            # Fallback if we can't determine the current site
            articles = NewsArticlePage.objects.live().order_by('-date')[:10]
        
        context['articles'] = articles
        return context
    
    class Meta:
        icon = 'list-ul'
        template = 'blocks/top_articles_block.html'
        label = 'Top Articles'


class VerticalLineBlock(StructBlock):
    # Base structure for both timelines and mission/vision
    
    title = CharBlock(required=False)
    content = TextBlock()
    date = DateTimeBlock(
        required=False,
        format="%Y-%m-%d",  # Hide time portion
        help_text="For timeline entries only"
    )
    learn_more = PageChooserBlock(required=False, help_text="Choose a page to link to for 'Learn More'")
    class Meta:
        template = 'blocks/vertical_line_block.html'
        icon = 'placeholder'


class TimelineSection(StructBlock):
    timeline_items = ListBlock(VerticalLineBlock())  # Note: renamed from timeline_item

    class Meta:
        template = 'blocks/vertical_line_block.html'
        icon = 'date'

class MissionVisionSection(StructBlock):
    statement_items = ListBlock(VerticalLineBlock())  # Note: renamed from statement_item

    class Meta:
        template = 'blocks/vertical_line_block.html'
        icon = 'doc-full'


class TeamMemberBlock(blocks.StructBlock):
    """Team members list with image, name, and role"""
    title = blocks.CharBlock(required=False, default="Meet the Team")
    team_members = blocks.ListBlock(
        blocks.StructBlock([
            ('name', blocks.CharBlock(required=True)),
            ('role', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=True)),
            ('bio', blocks.RichTextBlock(required=False)),
            ('facebook_link', blocks.URLBlock(required=False, help_text="Facebook profile link")),
            ('instagram_link', blocks.URLBlock(required=False, help_text="Instagram profile link")),
            ('twitter_link', blocks.URLBlock(required=False, help_text="Twitter profile link")),
        ])
    )

    class Meta:
        icon = 'group'
        template = 'blocks/team_member_block.html'


class StatisticItemBlock(blocks.StructBlock):
    """Individual statistic item with number and description"""
    number = blocks.CharBlock(
        required=True,
        help_text="The main number/percentage to display (e.g. '97%', '286')"
    )
    description = blocks.CharBlock(
        required=True,
        help_text="The description text below the number"
    )
    is_percentage = blocks.BooleanBlock(
        required=False,
        default=False,
        help_text="Check if this number represents a percentage"
    )

class StatisticsBlock(blocks.StructBlock):
    """A grid of statistics, each with a number and description"""
    title = blocks.CharBlock(
        required=False,
        help_text="Optional title for the statistics section"
    )
    statistics = blocks.ListBlock(
        StatisticItemBlock(),
        min_num=1,
        max_num=4,
        help_text="Add between 1 and 4 statistics"
    )
    background_style = blocks.ChoiceBlock(
        choices=[
            ('light', 'Light Blue'),
            ('dark', 'Deep Blue'),
            ('gradient', 'Blue Gradient'),
            ('transparent', 'Transparent'),
        ],
        default='light',
        help_text="Choose the background style for the statistics section"
    )

    class Meta:
        icon = 'chart'
        template = 'blocks/statistics_block.html'


class TestimonialItemBlock(blocks.StructBlock):
    """Individual testimonial with video"""
    video = EmbedBlock(required=True, help_text="Add a YouTube video URL")
    name = blocks.CharBlock(required=True, help_text="Name of the person giving testimonial")
    role = blocks.CharBlock(required=False, help_text="Role or title of the person")
    quote = blocks.TextBlock(required=False, help_text="Short quote or testimonial text")

class TestimonialsBlock(blocks.StructBlock):
    """Grid of video testimonials with hover preview"""
    title = blocks.CharBlock(required=False, default="What People Say")
    testimonials = blocks.ListBlock(
        TestimonialItemBlock(),
        max_num=4,
        min_num=1,
        help_text="Add between 1 and 4 video testimonials"
    )
    
    class Meta:
        icon = 'openquote'
        template = 'blocks/testimonials_block.html'


class NotificationBannerBlock(blocks.StructBlock):
    """
    Notification banner to be displayed at the top of the navbar
    """
    text = blocks.RichTextBlock(required=True, help_text="Notification text content")
    is_enabled = blocks.BooleanBlock(required=False, default=True, help_text="Enable or disable this notification")
    style = blocks.ChoiceBlock(
        choices=[
            ('info', 'Information (Blue)'),
            ('warning', 'Warning (Yellow)'),
            ('danger', 'Alert (Red)'),
            ('success', 'Success (Green)'),
            ('primary', 'Primary (Brand Color)'),
        ],
        default='info',
        help_text="Choose the style of notification"
    )
    icon = blocks.CharBlock(required=False, help_text="Optional Font Awesome icon name (e.g. 'fa-info-circle')")
    is_dismissible = blocks.BooleanBlock(required=False, default=True, help_text="Allow users to dismiss this notification")
    link_text = blocks.CharBlock(required=False, help_text="Optional link text")
    link_url = blocks.URLBlock(required=False, help_text="Optional link URL")
    
    class Meta:
        icon = 'warning'
        template = 'blocks/notification_banner_block.html'


class MainPersonMassage(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True, label="Title (e.g., General Mannager)")
    name = blocks.CharBlock(required=True, label="Name (e.g., Mr. Abdillahi Abdillahi)")
    text = blocks.TextBlock(required=True)
    background_color = blocks.ChoiceBlock(
        choices=[
            ('green', 'Green'),
            ('blue', 'Blue'),
            ('purple', 'Purple'),
            ('orange', 'Orange'),
            # Add more color choices as needed
        ],
        default='green',
        label="Background Color"
    )

    class Meta:
        template = 'blocks/mainperson_and_text_block.html'
        icon = 'card'


# Main StreamField block for use in page models
class BaseStreamBlock(blocks.StreamBlock):
    """
    Main streamfield block to be inherited by page models
    """
    heading = HeadingBlock()
    paragraph = blocks.RichTextBlock(icon='pilcrow')
    quote = QuoteBlock()
    cta = CallToActionBlock()
    accordion = AccordionBlock()
    two_column = TwoColumnBlock()
    images = ImageBlock()
    VideoBlock = VideoBlock()
 
    class Meta:
        icon = 'placeholder'



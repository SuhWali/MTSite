from django.db import models

# Create your models here.
from core.blocks import CarouselBlock
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from core.blocks import TimelineSection, MissionVisionSection, TeamMemberBlock, CardBlock, HeadingBlock, CallToActionBlock

class AboutPage(Page):
    """About page"""
    template = 'about/about_page.html'
 
    content = StreamField(
        [
            ('carousel', CarouselBlock()),
            # ('timeline', TimelineSection()),
            ('mission_vision', MissionVisionSection()),
            ('team_members', TeamMemberBlock()),
            ('cards', CardBlock()),
            ('heading', HeadingBlock()),
            ('call_to_action', CallToActionBlock()),
        ],
        blank=True,
        use_json_field=True,
    )
    
    content_panels = Page.content_panels + [

        FieldPanel('content'),
    ]

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
    

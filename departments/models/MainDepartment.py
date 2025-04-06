from django.db import models

# Create your models here.

from core.blocks import CarouselBlock
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from core.blocks import CardBlock, HeadingBlock, StatisticsBlock, AccordionBlock, SubscribeBlock


class MainPage(Page):
    template = 'departments/main_department.html'

    subpage_types = ['departments.SubDepartmentPage']  # Restricts subpages to SubDepartmentPage only
 
    content = StreamField(
        [
            ('carousel', CarouselBlock()),
            ('statistics', StatisticsBlock()),
            ('card', CardBlock()),
            ('heading', HeadingBlock()),
            ('accordion', AccordionBlock()),
            ('subscribe', SubscribeBlock()),
            # ('timeline', TimelineSection()),
            # ('mission_vision', MissionVisionSection()),
            # ('team_members', TeamMemberBlock()),
            # ('cards', CardBlock()),
            # ('heading', HeadingBlock()),
            # ('call_to_action', CallToActionBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Main Department"
        verbose_name_plural = "Main Departments"

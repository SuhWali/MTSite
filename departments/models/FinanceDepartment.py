from django.db import models
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from core.blocks import (
    CarouselBlock,
    CardBlock,
    HeadingBlock,
    StatisticsBlock,
    TeamMemberBlock,
    SubscribeBlock,
)




class FinanceDepartmentPage(Page):
    template = 'departments/finance_department.html'
    parent_page_types = ['departments.MainPage']  # Restricts parent to MainPage only
    
    content = StreamField(
        [
            ('carousel', CarouselBlock()),
            ('statistics', StatisticsBlock()),
            ('card', CardBlock()),
            ('team_members', TeamMemberBlock()),
            ('heading', HeadingBlock()),
            ('subscribe', SubscribeBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Finance Department"
        verbose_name_plural = "Finance Departments" 
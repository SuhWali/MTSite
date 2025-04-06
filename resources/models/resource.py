from django.db import models

# Create your models here.

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField


from core.blocks import CarouselBlock, BaseStreamBlock


class Resource(Page):
    """
    A page that represents a resource.
    """

    template = "resources/resource.html"

    parent_page_types = ["resources.ResourceIndexPage"]

    body = StreamField(
        [
            ("carousel", CarouselBlock()),
            ("Base_block", BaseStreamBlock())
        ],
        blank=True,
        use_json_field=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Resource Page"
        verbose_name_plural = "Resource Pages"

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField


from core.blocks import CarouselBlock





class ResourceIndexPage(Page):
    """
    A page that lists all resources.
    """

    template = "resources/resource_index.html"
    subpage_types = ["resources.Resource"]

    body = StreamField(
        [
            ("carousel", CarouselBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["resources"] = self.get_children().live()
        return context
    class Meta:
        verbose_name = "Resource Index Page"
        verbose_name_plural = "Resource Index Pages"

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.images import get_image_model_string
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtailmenus.models import AbstractMainMenuItem

# Add fields for translation (English, Somali, Arabic)
class MenuItem(AbstractMainMenuItem):
    parent = ParentalKey(
        'wagtailmenus.MainMenu',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='submenu_items'
    )



    # Add dropdown for translation (English, Somali, Arabic)

    Language_choices = [
        ('en', 'English'),
        ('so', 'Somali'),
        ('ar', 'Arabic'),
    ]

    language = models.CharField(max_length=2, choices=Language_choices, default='en')

    panels = [


        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('url_append'),
        FieldPanel('link_text'),
        FieldPanel('language'),
        FieldPanel('allow_subnav'),
    ]

    def __str__(self):
        return self.label


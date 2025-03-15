from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel



from core.blocks import TopArticlesBlock, CarouselBlock, SubscribeBlock, AccordionBlock, ImageBlock

class HomePage(Page):
    template = "home/home_page.html"


    # add the Hero section of HomePage:
 

    header = StreamField(
        [
        ('header', CarouselBlock()),
        
        ],
        blank=True,
        null=True
    )

    top_articles = StreamField(
        [
        ('top_articles', TopArticlesBlock()),
        ],
        blank=True,
        null=True
    )
    subscribe = StreamField(
        [
        ('subscribe', SubscribeBlock()),
        ],
        blank=True,
        null=True
    )
    accordion = StreamField(
        [
        ('accordion', AccordionBlock()),
        ],
        blank=True,
        null=True
    )   
    image = StreamField(
        [
        ('image', ImageBlock()),
        ],
        blank=True,
        null=True
    )


    body = RichTextField(blank=True)

    # content_panels = Page.content_panels + ["body"]

        # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
         
                FieldPanel("header"),
                FieldPanel("accordion"),
                FieldPanel("image"),
                FieldPanel('body'),
                FieldPanel("top_articles"),
                FieldPanel("subscribe"),
                
                
            ],
            heading="Hero section",
        ),
       
    ]

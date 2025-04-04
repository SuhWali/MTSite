from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from wagtail import blocks



from core.blocks import TopArticlesBlock, CarouselBlock, SubscribeBlock, AccordionBlock, ImageBlock, TestimonialsBlock, CardBlock, NotificationBannerBlock, MainPersonMassage

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

    main_body = StreamField(
        [
        ('main_person', MainPersonMassage()),
        ('top_articles', TopArticlesBlock()),
        ('subscribe', SubscribeBlock()),
        ('accordion', AccordionBlock()),
        ('image', ImageBlock()),
        ('body', blocks.RichTextBlock()),
        ('testimonials', TestimonialsBlock()),
        ('card', CardBlock()),
        ],
        blank=True,
        null=True
    )

    notification_banner = StreamField(
        [
            ('notification_banner', NotificationBannerBlock()),
        ],
        blank=True,
        null=True,
        use_json_field=True,
        help_text="Add a notification banner to the top of the page"
    )

    # body = RichTextField(blank=True)

    # content_panels = Page.content_panels + ["body"]

        # modify your content_panels:
    content_panels = Page.content_panels + [
        FieldPanel("notification_banner"),
        FieldPanel("header"),
        MultiFieldPanel(
            [
         
                FieldPanel('main_body'),
                # FieldPanel('body'),
             
                
            ],
            
            heading="Hero section",
        ),
       
    ]

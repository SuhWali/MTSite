from django.db import models
from django.core.validators import MinValueValidator
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractForm
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.search import index
from modelcluster.fields import ParentalKey
from django.utils import timezone
from core.blocks import CarouselBlock



class ApplicationFormField(AbstractFormField):
    page = ParentalKey(
        'ApplicationTrackingPage',
        on_delete=models.CASCADE,
        related_name='form_fields'
    )

    panels = [
        FieldPanel('label'),
        FieldPanel('help_text'),
        FieldPanel('required'),
        FieldPanel('field_type', classname="formbuilder-type"),
        FieldPanel('choices'),
        FieldPanel('default_value'),
    ]

    class Meta:
        ordering = ['sort_order']
        verbose_name = "Form Field"
        verbose_name_plural = "Form Fields"

class ApplicationTrackingPage(AbstractForm):
    intro = RichTextField(
        blank=True,
        help_text="Introduction text for the application page"
    )
    deadline = models.DateTimeField(
        help_text="Application deadline",
        null=True,
        blank=True
    )
    
    content = StreamField(
        [

            ('carousel', CarouselBlock()),


        ],
        blank=True,
        use_json_field=True,


    )

    
    # Form settings
    thank_you_text = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    content_panels = AbstractForm.content_panels + [
        FieldPanel('intro'),
        FieldPanel('deadline'),
        MultiFieldPanel([
            FieldPanel('content'),
         
        ], heading="Carousel Content"),
        InlinePanel('form_fields', label="Form Fields"),
        FieldPanel('thank_you_text', heading="Thank You Text"),
    ]

    form_builder = FormBuilder

    def get_form_fields(self):
        return self.form_fields.all()
    
    def get_data_fields(self):
        data_fields = [
            ('submission_date', 'Submission Date'),
        ]
        data_fields += super().get_data_fields()
        return data_fields
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # You can add custom form processing here
        return form

    def get_form_class(self):
        return super().get_form_class()

    class Meta:
        verbose_name = "Application Tracking Page"

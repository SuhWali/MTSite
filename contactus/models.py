from django.db import models

# Create your models here.

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)

from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractForm

from wagtailcaptcha.models import WagtailCaptchaForm


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')

class FormPage(WagtailCaptchaForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        # MultiFieldPanel([
        #     FieldRowPanel([
        #         FieldPanel('from_address', classname="col6"),
        #         FieldPanel('to_address', classname="col6"),
        #     ]),
        #     FieldPanel('subject'),
        # ], "Email"),
    ]
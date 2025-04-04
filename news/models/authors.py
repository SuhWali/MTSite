
from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from wagtail.search import index

@register_snippet
class Author(index.Indexed, models.Model):
    """
    Author snippet model for reuse across the site
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    bio = RichTextField(blank=True)
    email = models.EmailField(blank=True)
    twitter_handle = models.CharField(max_length=50, blank=True)

    # search_fields = [
    #     index.SearchField('first_name', boost=10),
    #     index.SearchField('last_name', boost=10)
    # ]
    
    panels = [
        MultiFieldPanel([
            FieldPanel('first_name'),
            FieldPanel('last_name'),
        ], heading="Name"),
        FieldPanel('photo'),
        FieldPanel('bio'),
        MultiFieldPanel([
            FieldPanel('email'),
            FieldPanel('twitter_handle'),
        ], heading="Contact Information"),
    ]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['last_name', 'first_name']

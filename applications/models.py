# from django.db import models
# from wagtail.models import Page, Orderable
# from wagtail.fields import StreamField, RichTextField
# from wagtail.admin.panels import FieldPanel, InlinePanel
# from modelcluster.fields import ParentalKey
# from core.blocks import CarouselBlock, CardBlock
# from wagtail.contrib.forms.models import AbstractForm, AbstractFormField

# class JobPost(Orderable):
#     page = ParentalKey('CareeJobDetailPagersPage', on_delete=models.CASCADE, related_name='jobs')
#     title = models.CharField(max_length=255)
#     type = models.CharField(max_length=50, choices=[
#         ('full-time', 'Full Time'),
#         ('part-time', 'Part Time'),
#         ('internship', 'Internship'),
#         ('contract', 'Contract'),
#     ])
#     location = models.CharField(max_length=255)
#     department = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     posted_date = models.DateField(auto_now_add=True)
#     closing_date = models.DateField(null=True, blank=True)
#     description = RichTextField()
#     requirements = RichTextField()
#     responsibilities = RichTextField()

#     panels = [
#         FieldPanel('title'),
#         FieldPanel('type'),
#         FieldPanel('location'),
#         FieldPanel('department'),
#         FieldPanel('is_active'),
#         FieldPanel('closing_date'),
#         FieldPanel('description'),
#         FieldPanel('requirements'),
#         FieldPanel('responsibilities'),
#     ]

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Job Posting"
#         verbose_name_plural = "Job Postings"

# class CareersPage(Page):
#     template = "applications/careers_page.html"
    
#     header = StreamField([
#         ('header', CarouselBlock()),
#     ], blank=True, null=True, use_json_field=True)
    
#     intro = RichTextField(blank=True)
    
#     content_panels = Page.content_panels + [
#         FieldPanel("header"),
#         FieldPanel("intro"),
#         InlinePanel("jobs", label="Job Postings"),
#     ]

#     def get_context(self, request, *args, **kwargs):
#         context = super().get_context(request, *args, **kwargs)
#         context['active_jobs'] = self.jobs.filter(is_active=True).order_by('-posted_date')
#         context['closed_jobs'] = self.jobs.filter(is_active=False).order_by('-closing_date')
#         return context

# class JobApplicationField(AbstractFormField):
#     page = ParentalKey('JobDetailPage', on_delete=models.CASCADE, related_name='form_fields')

# class JobDetailPage(AbstractForm):
#     template = "applications/job_detail_page.html"
#     landing_page_template = "applications/application_success.html"
    
#     job = models.ForeignKey(
#         JobPost,
#         on_delete=models.CASCADE,
#         related_name='detail_pages'
#     )
#     application_form_title = models.CharField(max_length=255, default="Apply Now")
#     thank_you_text = RichTextField(blank=True)
    
#     content_panels = AbstractForm.content_panels + [
#         FieldPanel("job"),
#         FieldPanel("application_form_title"),
#         InlinePanel('form_fields', label="Form fields"),
#         FieldPanel('thank_you_text'),
#     ]

#     def get_context(self, request, *args, **kwargs):
#         context = super().get_context(request, *args, **kwargs)
#         context['job'] = self.job
#         return context

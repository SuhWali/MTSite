# from wagtail import hooks
# from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
# from wagtail.admin.action_menu import ActionMenuItem
# from .models import ApplicationTrackingPage, ApplicationFormField

# @hooks.register('register_page_types')
# def register_page_types():
#     return [ApplicationTrackingPage]

# class ApplicationFormFieldAdmin(ModelAdmin):
#     model = ApplicationFormField
#     menu_label = 'Application Form Fields'
#     menu_icon = 'form'
#     list_display = ('label', 'field_type', 'required', 'sort_order')
#     list_filter = ('field_type', 'required')
#     search_fields = ('label',)
#     ordering = ('sort_order',)
#     # Prevent adding form fields directly through modeladmin
#     inspect_view_enabled = True
#     add_to_settings_menu = False
#     exclude_from_explorer = False

# modeladmin_register(ApplicationFormFieldAdmin)

# # Custom menu item for viewing submissions
# @hooks.register('register_page_action_menu_item')
# def register_view_submissions_menu_item():
#     return ActionMenuItem(
#         'View Submissions',
#         lambda page: f'/admin/forms/submissions/{page.id}/',
#         name='view-submissions',
#         icon_name='doc-full',
#         order=10
#     )

# # Only show the submissions menu item for ApplicationTrackingPage with submissions
# @hooks.register('construct_page_action_menu')
# def filter_page_action_menu_items(menu_items, request, context):
#     page = context.get('page')
    
#     # If not an ApplicationTrackingPage, remove the view-submissions button
#     if not isinstance(page, ApplicationTrackingPage):
#         menu_items = [item for item in menu_items if item.name != 'view-submissions']
#         return menu_items
    
#     # If it is an ApplicationTrackingPage, check if there are submissions
#     from wagtail.contrib.forms.models import FormSubmission
#     has_submissions = FormSubmission.objects.filter(page_id=page.id).exists()
    
#     if not has_submissions:
#         # Remove the view-submissions button if there are no submissions
#         menu_items = [item for item in menu_items if item.name != 'view-submissions']
    
#     return menu_items

# Generated by Django 5.1.7 on 2025-04-02 15:11

import django.db.models.deletion
import modelcluster.fields
import wagtailmenus.models.menuitems
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailmenus', '0023_remove_use_specific'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='link to a custom URL')),
                ('url_append', models.CharField(blank=True, help_text="Use this to optionally append a #hash or querystring to the above page's URL.", max_length=255, verbose_name='append to URL')),
                ('handle', models.CharField(blank=True, help_text='Use this field to optionally specify an additional value for each menu item, which you can then reference in custom menu templates.', max_length=100, verbose_name='handle')),
                ('link_text', models.CharField(blank=True, help_text="Provide the text to use for a custom URL, or set on an internal page link to use instead of the page's title.", max_length=255, verbose_name='link text')),
                ('allow_subnav', models.BooleanField(default=True, help_text="NOTE: The sub-menu might not be displayed, even if checked. It depends on how the menu is used in this project's templates.", verbose_name='allow sub-menu for this item')),
                ('label_en', models.CharField(blank=True, max_length=255, null=True)),
                ('label_so', models.CharField(blank=True, max_length=255, null=True)),
                ('label_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.page', verbose_name='link to an internal page')),
                ('parent', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submenu_items', to='wagtailmenus.mainmenu')),
            ],
            options={
                'verbose_name': 'menu item',
                'verbose_name_plural': 'menu items',
                'ordering': ('sort_order',),
                'abstract': False,
            },
            bases=(models.Model, wagtailmenus.models.menuitems.MenuItem),
        ),
    ]

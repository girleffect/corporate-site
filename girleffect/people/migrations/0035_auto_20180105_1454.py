# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-05 14:54
from __future__ import unicode_literals

from django.db import migrations
import girleffect.utils.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailsnippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0034_add_new_carousel_block_hex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpage',
            name='biography',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('body_text', wagtail.wagtailcore.blocks.StructBlock((('body', wagtail.wagtailcore.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr'], label='Body Text')), ('customisation', wagtail.wagtailcore.blocks.StructBlock((('background_image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('background_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False)), ('body_heading_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False))), required=False))))), ('large_text', wagtail.wagtailcore.blocks.StructBlock((('body', wagtail.wagtailcore.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], label='Large Text', max_length=350, required=False)), ('customisation', wagtail.wagtailcore.blocks.StructBlock((('background_image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('background_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False)), ('body_heading_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False))), required=False))))), ('extendable_body', wagtail.wagtailcore.blocks.StructBlock((('body_upper', wagtail.wagtailcore.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr'], label='Body Text')), ('extend_button_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Customise text for the extend button', max_length=80, required=False)), ('collapse_button_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Customise text for the collapse button', max_length=80, required=False)), ('body_lower', wagtail.wagtailcore.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr'], label='Body Text')), ('customisation', wagtail.wagtailcore.blocks.StructBlock((('background_image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('background_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False)), ('body_heading_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False))), required=False))))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quotes', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(max_length=80, required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], max_length=255, required=True)), ('citation', wagtail.wagtailcore.blocks.CharBlock(max_length=80, required=False)), ('link_block', wagtail.wagtailcore.blocks.StructBlock((('external_link', wagtail.wagtailcore.blocks.URLBlock(label='External Link', required=False)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(label='Internal Link', required=False)), ('internal_link_anchor', wagtail.wagtailcore.blocks.CharBlock(label='Internal Link anchor', required=False)), ('document_link', wagtail.wagtaildocs.blocks.DocumentChooserBlock(label='Document Link', required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(label='Link Text', max_length=255, required=False))), required=False)), ('drop_shadow_options', wagtail.wagtailcore.blocks.StructBlock((('drop_shadow_is_on', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Show or hide drop shadow', label='Drop Shadow Toggle', required=False)), ('text_hex', wagtail.wagtailcore.blocks.CharBlock(label='Text Hex Code', max_length=7, required=False))))), ('quote_mark_hex', wagtail.wagtailcore.blocks.CharBlock(label='Quote Mark Hex Code', max_length=7, required=False)))), icon='openquote', template='blocks/quote_block.html')), ('customisation', wagtail.wagtailcore.blocks.StructBlock((('background_image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('background_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False)), ('heading_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False))), required=False))))), ('video', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(max_length=30, required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], max_length=255, required=False)), ('youtube_embed', wagtail.wagtailembeds.blocks.EmbedBlock(help_text="Your YouTube URL goes here. Only YouTube video URLs will be accepted.            The custom 'play' button will be created for valid YouTube URLs.", label='YouTube Video URL')), ('link', wagtail.wagtailcore.blocks.StructBlock((('external_link', wagtail.wagtailcore.blocks.URLBlock(label='External Link', required=False)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(label='Internal Link', required=False)), ('internal_link_anchor', wagtail.wagtailcore.blocks.CharBlock(label='Internal Link anchor', required=False)), ('document_link', wagtail.wagtaildocs.blocks.DocumentChooserBlock(label='Document Link', required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(label='Link Text', max_length=255, required=False))), required=False)), ('customisation', wagtail.wagtailcore.blocks.StructBlock((('background_image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('background_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False))), required=False))), label='Girl Effect YouTube Video')), ('slider', wagtail.wagtailcore.blocks.StructBlock((('slider_delay', wagtail.wagtailcore.blocks.IntegerBlock(help_text='Enter the milliseconds of the delay between each slide', required=False)), ('slider_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('overview_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Slider item overview title', max_length=80, required=False)), ('overview_title_shadow', wagtail.wagtailcore.blocks.StructBlock((('drop_shadow_is_on', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Show or hide drop shadow', label='Drop Shadow Toggle', required=False)), ('text_hex', wagtail.wagtailcore.blocks.CharBlock(label='Text Hex Code', max_length=7, required=False))), required=False)), ('overview_text', wagtail.wagtailcore.blocks.TextBlock(help_text='Slider item overview text', max_length=255, required=False)), ('overview_text_shadow', wagtail.wagtailcore.blocks.StructBlock((('drop_shadow_is_on', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Show or hide drop shadow', label='Drop Shadow Toggle', required=False)), ('text_hex', wagtail.wagtailcore.blocks.CharBlock(label='Text Hex Code', max_length=7, required=False))), required=False)), ('textbox_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Slider item textbox title', max_length=30, required=False)), ('textbox_text', wagtail.wagtailcore.blocks.TextBlock(help_text='Slider item textbox text', max_length=75, required=False)), ('textbox_link', wagtail.wagtailcore.blocks.StructBlock((('external_link', wagtail.wagtailcore.blocks.URLBlock(label='External Link', required=False)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(label='Internal Link', required=False)), ('internal_link_anchor', wagtail.wagtailcore.blocks.CharBlock(label='Internal Link anchor', required=False)), ('document_link', wagtail.wagtaildocs.blocks.DocumentChooserBlock(label='Document Link', required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(label='Link Text', max_length=255, required=False))), required=False))))))))), ('carousel_block', wagtail.wagtailcore.blocks.StreamBlock((('carousel_item', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('overview_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Slider item overview title', max_length=80, required=False)), ('overview_title_shadow', wagtail.wagtailcore.blocks.StructBlock((('drop_shadow_is_on', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Show or hide drop shadow', label='Drop Shadow Toggle', required=False)), ('text_hex', wagtail.wagtailcore.blocks.CharBlock(label='Text Hex Code', max_length=7, required=False))), required=False)), ('overview_text', wagtail.wagtailcore.blocks.TextBlock(help_text='Slider item overview text', max_length=255, required=False)), ('overview_text_shadow', wagtail.wagtailcore.blocks.StructBlock((('drop_shadow_is_on', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Show or hide drop shadow', label='Drop Shadow Toggle', required=False)), ('text_hex', wagtail.wagtailcore.blocks.CharBlock(label='Text Hex Code', max_length=7, required=False))), required=False)), ('textbox_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Slider item textbox title', max_length=30, required=False)), ('textbox_text', wagtail.wagtailcore.blocks.TextBlock(help_text='Slider item textbox text', max_length=75, required=False)), ('textbox_link', wagtail.wagtailcore.blocks.StructBlock((('external_link', wagtail.wagtailcore.blocks.URLBlock(label='External Link', required=False)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(label='Internal Link', required=False)), ('internal_link_anchor', wagtail.wagtailcore.blocks.CharBlock(label='Internal Link anchor', required=False)), ('document_link', wagtail.wagtaildocs.blocks.DocumentChooserBlock(label='Document Link', required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(label='Link Text', max_length=255, required=False))), required=False)), ('slide_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title to appear at bottom of carousel, for example "Youth Brands"', required=False)), ('slide_logo', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('slide_title_hex', wagtail.wagtailcore.blocks.CharBlock(help_text='Add valid hex for slide title and chevron colours.', max_length=7))))),), label='Carousel', max_num=3, min_num=2)), ('media_text_overlay', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Appears above the module.', label='Title Text', max_length=25, required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('logo', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Title Logo', required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], max_length=75, required=False)), ('link', wagtail.wagtailcore.blocks.StructBlock((('external_link', wagtail.wagtailcore.blocks.URLBlock(label='External Link', required=False)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(label='Internal Link', required=False)), ('internal_link_anchor', wagtail.wagtailcore.blocks.CharBlock(label='Internal Link anchor', required=False)), ('document_link', wagtail.wagtaildocs.blocks.DocumentChooserBlock(label='Document Link', required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(label='Link Text', max_length=255, required=False))), required=False)), ('customisation', wagtail.wagtailcore.blocks.StructBlock((('background_image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('background_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False))), required=False))), label='Full Width Media with Text Overlay')), ('list_block', wagtail.wagtailcore.blocks.StructBlock((('list_block', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(max_length=80, required=False)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], icon='pilcrow', max_length=250, required=False)), ('link', wagtail.wagtailcore.blocks.StructBlock((('external_link', wagtail.wagtailcore.blocks.URLBlock(label='External Link', required=False)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(label='Internal Link', required=False)), ('internal_link_anchor', wagtail.wagtailcore.blocks.CharBlock(label='Internal Link anchor', required=False)), ('document_link', wagtail.wagtaildocs.blocks.DocumentChooserBlock(label='Document Link', required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(label='Link Text', max_length=255, required=False))), required=False)))))), ('customisation', wagtail.wagtailcore.blocks.StructBlock((('background_image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('background_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False)), ('heading_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False))), required=False))))), ('link_row', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('external_link', wagtail.wagtailcore.blocks.URLBlock(label='External Link', required=False)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(label='Internal Link', required=False)), ('internal_link_anchor', wagtail.wagtailcore.blocks.CharBlock(label='Internal Link anchor', required=False)), ('document_link', wagtail.wagtaildocs.blocks.DocumentChooserBlock(label='Document Link', required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(label='Link Text', max_length=255, required=False)))), icon='link', template='blocks/inline_link_block.html')), ('anchor', wagtail.wagtailcore.blocks.StructBlock((('anchor', wagtail.wagtailcore.blocks.CharBlock()),))), ('statistic', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(max_length=80, required=False)), ('statistics', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailsnippets.blocks.SnippetChooserBlock(girleffect.utils.models.Statistic))), ('link', wagtail.wagtailcore.blocks.StructBlock((('external_link', wagtail.wagtailcore.blocks.URLBlock(label='External Link', required=False)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(label='Internal Link', required=False)), ('internal_link_anchor', wagtail.wagtailcore.blocks.CharBlock(label='Internal Link anchor', required=False)), ('document_link', wagtail.wagtaildocs.blocks.DocumentChooserBlock(label='Document Link', required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(label='Link Text', max_length=255, required=False))), required=False)), ('customisation', wagtail.wagtailcore.blocks.StructBlock((('background_image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('background_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False)), ('heading_hex', wagtail.wagtailcore.blocks.CharBlock(max_length=7, required=False))), required=False))), label='Statistic Block')), ('call_to_action', wagtail.wagtailsnippets.blocks.SnippetChooserBlock(girleffect.utils.models.CallToActionSnippet, template='blocks/call_to_action.html'))), blank=True),
        ),
    ]

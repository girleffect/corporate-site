import re
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from wagtail.wagtailcore import blocks
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds import oembed_providers
from wagtail.wagtailembeds.finders.oembed import OEmbedFinder as OEmbedFinder
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock

from .models import CallToActionSnippet, Statistic


def validate_hex(value):
    return not value or re.match('^\#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$', value)


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class CustomisationBlock(blocks.StructBlock):
    """ For hex colours, background images """
    background_image = ImageChooserBlock(required=False)
    background_hex = blocks.CharBlock(max_length=7, required=False)

    class Meta:
        template = "blocks/customisation_block.html"

    def clean(self, value):
        value = super().clean(value)

        hex_fields = ['background_hex']
        errors = {field: ['Please enter a valid hex code'] for field in hex_fields if not validate_hex(value[field])}

        if value['background_image'] and value['background_hex']:
            error_message = ["Please select one of background image or background hex"]
            errors['background_image'] = error_message
            errors['background_hex'] = error_message

        if errors:
            raise ValidationError(
                "Validation error in CustomisationBlock",
                params=errors,
            )
        return value


class HeadingCustomisationBlock(CustomisationBlock):
    """ For hex colours, background images """
    heading_hex = blocks.CharBlock(max_length=7, required=False)

    def clean(self, value):
        errors = {}

        try:
            value = super().clean(value)
        except ValidationError as e:
            errors = e.params

        hex_fields = ['heading_hex']
        heading_errors = {field: ['Please enter a valid hex code'] for field in hex_fields if not validate_hex(value[field])}

        if heading_errors:
            errors.update(heading_errors)
            raise ValidationError(
                "Validation error in CustomisationBlock",
                params=errors,
            )
        return value


class BodyHeadingCustomisationBlock(CustomisationBlock):
    """ For hex colours, background images """
    body_heading_hex = blocks.CharBlock(max_length=7, required=False)

    def clean(self, value):
        errors = {}

        try:
            value = super().clean(value)
        except ValidationError as e:
            errors = e.params

        hex_fields = ['body_heading_hex']
        heading_errors = {field: ['Please enter a valid hex code'] for field in hex_fields if not validate_hex(value[field])}

        if heading_errors:
            errors.update(heading_errors)
            raise ValidationError(
                "Validation error in CustomisationBlock",
                params=errors,
            )
        return value


class LinkBlock(blocks.StructBlock):
    external_link = blocks.URLBlock(required=False, label="External Link")
    internal_link = blocks.PageChooserBlock(required=False, label="Internal Link")
    document_link = DocumentChooserBlock(required=False, label="Document Link")

    link_text = blocks.CharBlock(required=False, max_length=255, label="Link Text")

    def get_context(self, value, **kwargs):
        context = super().get_context(value, **kwargs)

        external_link = value.get('external_link')
        internal_link = value.get('internal_link')
        document_link = value.get('document_link')

        # URL
        if external_link:
            context['link_url'] = external_link
        elif internal_link:
            context['link_url'] = internal_link.url
        elif document_link:
            context['link_url'] = document_link.url

        # External link?
        if external_link:
            context['link_is_external'] = True
        else:
            context['link_is_external'] = False

        return context

    def clean(self, value):
        """
        Validate that exactly one of the link destination blocks is populated if the link text is populated
        """
        link_dest_block_names = [
            'internal_link',
            'document_link',
            'external_link',
        ]
        num_populated_blocks = 0

        for block_name in link_dest_block_names:
            if value[block_name]:
                num_populated_blocks += 1

        if num_populated_blocks > 1:
            error_messages = ["Link can only have one destination"]
            raise ValidationError(
                "Validation error in LinkBlock",
                params={block_name: error_messages for block_name in link_dest_block_names},
            )

        return super().clean(value)

    class Meta:
        template = "blocks/link_block.html"


class CarouselItemBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    label = blocks.CharBlock(
        max_length=30,
        help_text="Carousel item small label, for example Our Reach"
    )
    title = blocks.CharBlock(
        max_length=30,
        help_text="Carousel item large title"
    )
    text = blocks.RichTextBlock(
        max_length=75,
        required=False,
        help_text="Carousel item text",
        features=["bold", "italic", "ol", "ul", "link", "document-link"]
    )
    link = LinkBlock(required=False)

    class Meta:
        icon = "plus"
        template = "blocks/carousel_item_block.html"


class MediaTextOverlayBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        required=False,
        label="Title Text",
        max_length=25,
        help_text="Appears above the module."
    )
    image = ImageChooserBlock()
    logo = ImageChooserBlock(
        label="Title Logo",
        required=False
    )
    text = blocks.RichTextBlock(
        max_length=75,
        required=False,
        features=["bold", "italic", "ol", "ul", "link", "document-link"]
    )
    link = LinkBlock(required=False)
    customisation = CustomisationBlock(required=False)

    def clean(self, value):
        if value['title'] and value['logo']:
            error_messages = ["Please choose only one of logo or title."]
            raise ValidationError(
                "Validation error in MediaTextOverlayBlock",
                params={'title': error_messages, 'logo': error_messages},
            )
        if not value['title'] and not value['logo']:
            error_messages = ["Please choose a logo or title."]
            raise ValidationError(
                "Validation error in MediaTextOverlayBlock",
                params={'title': error_messages, 'logo': error_messages},
            )
        return super().clean(value)

    class Meta:
        icon = "image"
        template = "blocks/media_text_overlay_block.html"


class YouTubeEmbed(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, max_length=30)
    text = blocks.RichTextBlock(
        max_length=255,
        required=False,
        features=["bold", "italic", "ol", "ul", "link", "document-link"]
    )
    youtube_embed = EmbedBlock(
        label="YouTube Video URL",
        help_text="Your YouTube URL goes here. Only YouTube video URLs will be accepted.\
            The custom 'play' button will be created for valid YouTube URLs."
    )
    link = LinkBlock(required=False)
    customisation = CustomisationBlock(required=False)

    def clean(self, value):
        cleaned_data = super().clean(value)
        # Validating if URL is a valid YouTube URL
        youtube_embed = cleaned_data.get('youtube_embed').url
        youtube_finder = OEmbedFinder(providers=[oembed_providers.youtube])
        if not youtube_finder.accept(youtube_embed):
            e = ValidationError('URL must be a YouTube URL')
            raise ValidationError('Validation error in StructBlock', params={
                                  'youtube_embed': ErrorList([e])})
        return cleaned_data

    class Meta:
        icon = "media"
        template = "blocks/youtube_embed_block.html"


class QuoteBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=80, required=False)
    image = ImageChooserBlock(required=False)
    text = blocks.RichTextBlock(
        max_length=255,
        required=True,
        features=["bold", "italic", "ol", "ul", "link", "document-link"]
    )
    citation = blocks.CharBlock(
        required=False,
        max_length=80,
    )
    link_block = LinkBlock(required=False)
    drop_shadow_is_on = blocks.BooleanBlock(
        label="Drop Shadow Toggle",
        help_text="Show or hide drop shadow",
        required=False
    )
    text_hex = blocks.CharBlock(
        label="Quote Text Hex Code",
        max_length=7,
        required=False
    )
    quote_mark_hex = blocks.CharBlock(
        label="Quote Mark Hex Code",
        max_length=7,
        required=False
    )

    class Meta:
        template = "blocks/quote_item_block.html"

    def clean(self, value):
        value = super().clean(value)
        errors = {}

        hex_fields = ['text_hex', 'quote_mark_hex']
        errors = {field: ['Please enter a valid hex code'] for field in hex_fields if not validate_hex(value[field])}

        if errors:
            raise ValidationError(
                "Validation error in QuoteBlock",
                params=errors,
            )
        return value


class QuoteListBlock(blocks.StructBlock):
    quotes = blocks.ListBlock(
        QuoteBlock(),
        template="blocks/quote_block.html",
        icon="openquote"
    )
    customisation = HeadingCustomisationBlock(
        required=False
    )

    class Meta:
        icon = "openquote"
        template = "blocks/quote_block.html"


class ListItemBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(max_length=80, required=False)
    description = blocks.RichTextBlock(
        max_length=250,
        features=["bold", "italic", "link", "document-link"],
        required=False,
        icon="pilcrow"
    )
    link = LinkBlock(required=False)

    class Meta:
        icon = "list-ul"
        template = "blocks/list_column_item_block.html"


class ContentSectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(classname="full title", required=False)
    body_text = blocks.RichTextBlock(label="Body Text")
    image = ImageChooserBlock(required=False)
    link = LinkBlock(required=False)

    class Meta:
        icon = "fa-newspaper-o"


class StatisticBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=80, required=False)
    statistics = blocks.ListBlock(
        SnippetChooserBlock(Statistic),
    )
    link = LinkBlock(required=False)
    customisation = HeadingCustomisationBlock(
        required=False
    )

    class Meta:
        icon = "snippet"
        template = "blocks/statistic_block.html"


class BlockQuote(blocks.StructBlock):
    quote = blocks.TextBlock()
    citation = blocks.CharBlock(required=False)

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote_block.html"


class LargeTextBlock(blocks.StructBlock):
    body = blocks.RichTextBlock(
        label="Large Text",
        max_length=350,
        features=["bold", "italic", "link", "document-link"],
        required=False,
    )
    customisation = BodyHeadingCustomisationBlock(
        required=False
    )

    class Meta:
        icon = "pilcrow"
        template = "blocks/large_text_block.html"


class BodyTextBlock(blocks.StructBlock):
    body = blocks.RichTextBlock(
        label="Body Text",
        features=[
            "h2", "h3", "h4",
            "bold", "italic", "link",
            "ol", "ul", "hr"
        ],
    )
    customisation = BodyHeadingCustomisationBlock(
        required=False
    )

    class Meta:
        icon = "pilcrow"
        template = "blocks/body_text_block.html"


class ExtendableBodyTextBlock(blocks.StructBlock):
    body_upper = blocks.RichTextBlock(
        label="Body Text",
        features=[
            "h2", "h3", "h4",
            "bold", "italic", "link",
            "ol", "ul", "hr"
        ],
    )
    extend_button_text = blocks.CharBlock(
        max_length=80,
        required=False,
        help_text="Customise text for the extend button"
    )
    collapse_button_text = blocks.CharBlock(
        max_length=80,
        required=False,
        help_text="Customise text for the collapse button"
    )
    body_lower = blocks.RichTextBlock(
        label="Body Text",
        features=[
            "h2", "h3", "h4",
            "bold", "italic", "link",
            "ol", "ul", "hr"
        ],
    )

    customisation = BodyHeadingCustomisationBlock(
        required=False
    )

    class Meta:
        icon = "collapse-down"
        template = "blocks/extendable_body_text_block.html"


class ListColumnBlock(blocks.StructBlock):
    list_block = blocks.ListBlock(
        ListItemBlock()
    )
    customisation = HeadingCustomisationBlock(
        required=False
    )

    class Meta:
        template = "blocks/list_column_block.html"
        icon = "list-ul"


class StoryBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    body_text = BodyTextBlock()
    large_text = LargeTextBlock()
    extendable_body = ExtendableBodyTextBlock()
    image = ImageBlock()
    quote = QuoteListBlock()
    video = YouTubeEmbed(label="Girl Effect YouTube Video")
    carousel = blocks.ListBlock(
        CarouselItemBlock(),
        template="blocks/carousel_block.html",
        icon="image"
    )
    media_text_overlay = MediaTextOverlayBlock(
        label="Full Width Media with Text Overlay"
    )
    list_block = ListColumnBlock()
    link_row = blocks.ListBlock(
        LinkBlock(),
        template="blocks/inline_link_block.html",
        icon="link"
    )
    statistic = StatisticBlock(label="Statistic Block")
    call_to_action = SnippetChooserBlock(CallToActionSnippet, template="blocks/call_to_action.html")

    class Meta:
        template = "blocks/stream_block.html"


class ArticleBlock(StoryBlock):
    blockquote = BlockQuote()

    class Meta:
        template = "blocks/stream_block.html"

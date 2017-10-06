from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock

from .models import CallToActionSnippet


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class QuoteBlock(blocks.StructBlock):
    quote = blocks.CharBlock(classname="title")
    citation_link = blocks.URLBlock(required=False)

    class Meta:
        icon = "openquote"
        template = "blocks/quote_block.html"


# Main streamfield block to be inherited by Pages

class StoryBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    large_text = blocks.RichTextBlock(
        classname="large-text",
        label="Large Text",
        max_length=350,
        features=["bold", "italic", "link", "document-link"],
        required=False,
        icon="pilcrow"
    )
    image = ImageBlock()
    quote = QuoteBlock()
    embed = EmbedBlock()
    call_to_action = SnippetChooserBlock(CallToActionSnippet, template="includes/call_to_action.html")

    class Meta:
        template = "blocks/stream_block.html"

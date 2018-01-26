from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)

from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail.wagtailcore.fields import StreamField
from girleffect.wagtailsnippets.edit_handlers import SnippetChooserPanel
from girleffect.articles.models import ArticlePage
from girleffect.utils.models import (
    CallToActionSnippet,
    LinkFields,
    HeroVideoFields,
    SocialFields
)

from girleffect.utils.blocks import StoryBlock


class HomePage(Page, HeroVideoFields, SocialFields):
    introduction = models.TextField(blank=True, null=True)
    call_to_action = models.ForeignKey(CallToActionSnippet, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    overview_image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL
    )
    body = StreamField(StoryBlock(), null=True)

    content_panels = Page.content_panels + HeroVideoFields.content_panels + [
        FieldPanel('introduction'),
        StreamFieldPanel('body'),
        SnippetChooserPanel('call_to_action')
    ]

    @cached_property
    def articles(self):
        return ArticlePage.objects.all().live().public().order_by('-publication_date')[:6]

    promote_panels = (
        Page.promote_panels +  # slug, seo_title, show_in_menus, search_description
        SocialFields.promote_panels
    )

    def get_link_text(self):
        if self.link_text:
            return self.link_text

        if self.link_page:
            return self.link_page.title

        return ''

    # Only allow creating HomePages at the root level
    parent_page_types = ['wagtailcore.Page']

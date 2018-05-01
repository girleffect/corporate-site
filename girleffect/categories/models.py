from django.db import models

from girleffect.wagtailsnippets.models import SiteSpecificSnippetMixin, register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel


@register_snippet
class Category(SiteSpecificSnippetMixin, models.Model):
    name = models.TextField()

    panels = [
        FieldPanel('name', classname="full"),
    ]

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.blocks import CharBlock, RichTextBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class SimplePage(Page):
    content = models.TextField()

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('content'),
    ]


class StreamPage(Page):
    body = StreamField([
        ('text', CharBlock()),
        ('rich_text', RichTextBlock()),
    ])


class BusinessIndex(Page):
    """ Can be placed anywhere, can only have Business children """
    subpage_types = ['tests.BusinessChild', 'tests.BusinessSubIndex']


class BusinessSubIndex(Page):
    """ Can be placed under BusinessIndex, and have BusinessChild children """
    subpage_types = ['tests.BusinessChild']
    parent_page_types = ['tests.BusinessIndex']


class BusinessChild(Page):
    """ Can only be placed under Business indexes, no children allowed """
    subpage_types = []
    parent_page_types = ['tests.BusinessIndex', BusinessSubIndex]


class EventIndex(Page):
    subpage_types = ['EventPage']


class EventPage(Page):
    parent_page_types = ['EventIndex']
    subpage_types = []

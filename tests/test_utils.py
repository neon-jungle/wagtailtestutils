from __future__ import absolute_import, unicode_literals

import json

from django.utils import six
from wagtail.wagtailcore.models import Page, Site, PAGE_MODEL_CLASSES

from wagtailtestutils import WagtailPageTests

from .models import (
    BusinessChild, BusinessIndex, BusinessSubIndex, EventIndex, EventPage,
    SimplePage, StreamPage)


class TestWagtailPageTests(WagtailPageTests):
    def setUp(self):
        super(TestWagtailPageTests, self).setUp()
        site = Site.objects.get(is_default_site=True)
        self.root = site.root_page.specific

    def assertRaisesRegex(self, *args, **kwargs):
        if six.PY3:
            return super(TestWagtailPageTests, self).assertRaisesRegex(*args, **kwargs)
        else:
            return self.assertRaisesRegexp(*args, **kwargs)

    def test_assert_can_create_at(self):
        # It should be possible to create an EventPage under an EventIndex,
        self.assertCanCreateAt(EventIndex, EventPage)
        self.assertCanCreateAt(Page, EventIndex)
        # It should not be possible to create a SimplePage under a BusinessChild
        self.assertCanNotCreateAt(SimplePage, BusinessChild)

        # This should raise, as it *is not* possible
        with self.assertRaises(AssertionError):
            self.assertCanCreateAt(SimplePage, BusinessChild)
        # This should raise, as it *is* possible
        with self.assertRaises(AssertionError):
            self.assertCanNotCreateAt(EventIndex, EventPage)

    def test_assert_can_create(self):

        self.assertFalse(EventIndex.objects.exists())
        self.assertCanCreate(self.root, EventIndex, {
            'title': 'Event Index',
            'intro': '<p>Event intro</p>'})
        self.assertTrue(EventIndex.objects.exists())

        self.assertCanCreate(self.root, StreamPage, {
            'title': 'WebDev42',
            'body': json.dumps([
                {'type': 'text', 'value': 'Some text'},
                {'type': 'rich_text', 'value': '<p>Some rich text</p>'},
            ])})

    def test_assert_can_create_subpage_rules(self):
        simple_page = SimplePage(title='Simple Page', slug='simple')
        self.root.add_child(instance=simple_page)
        # This should raise an error, as a BusinessChild can not be created under a SimplePage
        with self.assertRaisesRegex(AssertionError, r'Can not create a tests.businesschild under a tests.simplepage'):
            self.assertCanCreate(simple_page, BusinessChild, {})

    def test_assert_can_create_validation_error(self):
        # This should raise some validation errors, complaining about missing
        # title and slug fields
        with self.assertRaisesRegex(AssertionError, r'\bslug:\n[\s\S]*\btitle:\n'):
            self.assertCanCreate(self.root, SimplePage, {})

    def test_assert_allowed_subpage_types(self):
        self.assertAllowedSubpageTypes(BusinessIndex, {BusinessChild, BusinessSubIndex})
        self.assertAllowedSubpageTypes(BusinessChild, {})
        self.assertAllowedSubpageTypes(Page, PAGE_MODEL_CLASSES)
        with self.assertRaises(AssertionError):
            self.assertAllowedSubpageTypes(BusinessSubIndex, {BusinessSubIndex, BusinessChild})

    def test_assert_allowed_parent_page_types(self):
        self.assertAllowedParentPageTypes(BusinessChild, {BusinessIndex, BusinessSubIndex})
        self.assertAllowedParentPageTypes(BusinessSubIndex, {BusinessIndex})
        self.assertAllowedParentPageTypes(BusinessIndex, PAGE_MODEL_CLASSES)
        with self.assertRaises(AssertionError):
            self.assertAllowedParentPageTypes(BusinessSubIndex, {BusinessSubIndex, BusinessIndex})

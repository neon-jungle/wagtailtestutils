.. _reference:

=========
Reference
=========

.. automodule:: wagtailtestutils.utils

WagtailPageTests
================

.. class:: WagtailPageTests

    .. automethod:: assertCanCreateAt

        Example:

        .. code-block:: python

            # You can create a ContentPage under a HomePage
            self.assertCanCreateAt(HomePage, ContentPage)

    .. automethod:: assertCanNotCreateAt

        Example:

        .. code-block:: python

            # You can not create a ContentPage under an EventPage
            self.assertCanNotCreateAt(EventPage, ContentPage)

    .. automethod:: assertCanCreate

        Example:

        .. code-block:: python

            # Get the HomePage
            root_page = HomePage.objects.get(pk=2)

            # Assert that a ContentPage can be made here, with this POST data
            self.assertCanCreate(root_page, ContentPage, {
                'title': 'About us',
                'body': 'Lorem ipsum dolor sit amet')

    .. automethod:: assertAllowedParentPageTypes

        Example:

        .. code-block:: python

            # A ContentPage can only be created under a HomePage
            # or another ContentPage
            self.assertAllowedParentPageTypes(
                ContentPage, {HomePage, ContentPage})

            # An EventPage can only be created under an EventIndex
            self.assertAllowedParentPageTypes(
                EventPage, {EventIndex})

    .. automethod:: assertAllowedSubpageTypes

        Example:

        .. code-block:: python

            # A ContentPage can only have other ContentPage children
            self.assertAllowedSubpageTypes(
                ContentPage, {ContentPage})

            # A HomePage can have ContentPage and EventIndex children
            self.assertAllowedParentPageTypes(
                HomePage, {ContentPage, EventIndex})

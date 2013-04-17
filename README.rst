Introduction
============

This product implements a viewlet that will add a second level navigation to site. It is meant to be used below the viewlet plone.global_sections, which lists main sections. The product is not meant for implementing dropdown menus, but only the second level that reacts to navigation. Similar menu concept is used by ie. SAP/R3, and the idea is that showing a context sensible part in the menus helps user with navigation.

Features:

- When the main section changes the second level reflects the children of that section
- The content item on selected path will have css class to signify that it is selected

Screenshot with very simple css:

.. image:: https://raw.github.com/collective/collective.secondlevel/master/docs/screenshot.png

Installation
============

- Install to Plone 
- Make sure the viewlet is in correct position (use @@manage-viewlets). It should be unless you have already customized viewlets.
- Develop CSS for the list. You can use the portal-globalnav as reference.
 

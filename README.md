Introduction
============

This product implements a viewlet that will add a second level navigation to site. It is meant to be used below the viewlet plone.global_sections, which lists main sections.

Features:

- When the main section changes the second level reflects the children of that section
- The content item on selected path will have css class to signify that it is selected

Installation
============

- Install and enable like any other Plone addon (not in pypi yet, copy to src - sorry)
- Make sure the viewlet is in correct position (use @@manage-viewlets)
- Develop CSS for the list. You can use the portal-globalnav probably as a starting point
 

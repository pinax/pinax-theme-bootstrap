Bootstrap Theme, for Pinax
==================================

A theme for Pinax based on the open source Bootstrap front-end framework.


Versions
--------

* Bootstrap v3.3.0
* Font Awesome v4.2.0
* jQuery v2.1.1


Quick Start
-----------

Include "pinax-theme-bootstrap" in your requirements file and include
"pinax_theme_bootstrap" and "bootstrapform" (which is installed alongside
this theme) in your INSTALLED APPS.

Add 'django.core.context_processors.request' and
"pinax_theme_bootstrap.context_processors.theme" to your TEMPLATE_CONTEXT_PROCESSORS
to ensure the user selector and site name work correctly.

Make sure both template loaders and staticfiles finders includes
app directories.

Site name comes from Sites fixture.

Your "site_base.html" should extend "theme_bootstrap/base.html" and should provide
"footer" and "nav" blocks (the latter should just be a ul of li of a links).

Your pages should have blocks "head_title" and "body" and should extend
"site_base.html".

The url name "home" should be defined as the homepage.


License & Attribution
---------------------

The Pinax Bootstrap theme is released under the MIT license.

This theme includes styles and scripts from the Bootstrap project,
which is (since v3.1.0) released under the MIT license.

For copies of both licenses, see LICENSE.

Includes icons from `Glyphicons Free <http://glyphicons.com/>`_, licensed
under `CC BY 3.0 <http://creativecommons.org/licenses/by/3.0/>`_.

Includes icons from
`Font Awesome <http://fortawesome.github.io/Font-Awesome/>`_.


.. _django-bootstrap-form: https://github.com/tzangms/django-bootstrap-form
.. _official migration guide: http://getbootstrap.com/getting-started/#migration
.. _PaginationTemplate: https://github.com/pinax/pinax-theme-bootstrap/blob/master/pinax_theme_bootstrap/templates/pagination/pagination.html
.. _django-pagination: https://github.com/ericflo/django-pagination

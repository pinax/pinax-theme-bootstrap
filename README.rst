Pinax Theme Bootstrap
==================================

.. image:: http://slack.pinaxproject.com/badge.svg
   :target: http://slack.pinaxproject.com/


Pinax
-------

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. 
This collection can be found at http://pinaxproject.com.


pinax-theme-bootstrap
----------------------

``pinax-theme-bootstrap`` is a theme for Pinax based on the open source Bootstrap front-end framework and
the Font Awesome icon library.


Getting Started
-----------------

Include ``pinax-theme-bootstrap`` in your requirements file and include
``pinax_theme_bootstrap`` and ``bootstrapform`` (which is installed alongside
this theme) in your ``INSTALLED APPS``.

Add ``django.core.context_processors.request`` and
``pinax_theme_bootstrap.context_processors.theme`` to your ``TEMPLATE_CONTEXT_PROCESSORS``
to ensure the user selector and site name work correctly.

Make sure both template loaders and staticfiles finders includes
app directories.

Site name comes from Sites fixture.

Your ``site_base.html`` should extend ``theme_bootstrap/base.html`` and should provide
``footer`` and ``nav`` blocks (the latter should just be a ul of li of a links).

Your pages should have blocks ``head_title`` and ``body`` and should extend
``site_base.html``.

The url name ``home`` should be defined as the homepage.


Dependencies
------------

* Bootstrap
* Font Awesome
* jQuery

We previously vendored these packages and had an undocumented build process
pre-configured in our starter projects that use this theme. This has gone the
way of the 80s hair band and we are now using proper packaging in the starter
projects.

The templates in this project are currently tested with the following versions:

* Bootstrap 3.3.5
* Font Awesome 4.4.0
* jQuery 2.1.4

If you are not using one of our starter projects, you will need to go about
setting up a build environment to use these libraries. We recommend using
`webpack <http://webpack.github.io/>`_ and installing these libraries with
``npm``.


Upgrade Notes
-------------

Upgrading to 6.0, you should be aware of a few changes:

* ``style_base`` and ``extra_style`` blocks have been merged into ``styles``
* ``script_base`` and ``extra_script`` blocks have been merged into ``scripts`` and
  the ``theme.js`` script is now loaded within a ``theme_script`` block after the
  ``scripts`` block. It now expects that you'll load the necessary ``jQuery``
  library at the project level in the ``scripts`` block.
* No vendored assets ship with the theme anymore. You are responsible for
  setting up your own static assets at the project level. We have made it easy
  by just using one of our starter projects.


Documentation
--------------

The Pinax documentation is available at http://pinaxproject.com/pinax/.


License
-------

The Pinax Bootstrap theme is released under the MIT license.


Code of Conduct
-----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/.


Pinax Project Blog and Twitter
--------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our blog http://blog.pinaxproject.com.



.. _django-bootstrap-form: https://github.com/tzangms/django-bootstrap-form
.. _PaginationTemplate: https://github.com/pinax/pinax-theme-bootstrap/blob/master/pinax_theme_bootstrap/templates/pagination/pagination.html
.. _django-pagination: https://github.com/ericflo/django-pagination

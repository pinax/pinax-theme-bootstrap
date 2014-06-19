Bootstrap Theme, for Pinax
==================================

A theme for Pinax based on the open source Bootstrap front-end framework.


Versions
--------

* Bootstrap v3.1.1
* Font Awesome v4.1.0

Quick Start
-----------

Include "pinax-theme-bootstrap" in your requirements file and include
"pinax_theme_bootstrap" and "bootstrapform" (which is installed alongside
this theme) in your INSTALLED APPS.

Make sure both template loaders and staticfiles finders includes
app directories.

Site name comes from Sites fixture.

Your "site_base.html" should extend "theme_bootstrap/base.html" and should provide
"footer" and "nav" blocks (the latter should just be a ul of li of a links).

Your pages should have blocks "head_title" and "body" and should extend
"site_base.html".

The url name "home" should be defined as the homepage.


Upgrade Notes
-------------

- To upgrade an existing site running on the prior version of this theme, it is
  recommended that you read through the `official migration guide`_.

- Forms Rendering: Versions prior to 4.0 used django-forms-bootstrap. We have switched
  this app to `django-bootstrap-form`_ so you'll need to make the necessary updates
  to your templates and INSTALLED_APPS.


Requirements
------------

This theme is officially supported when used in conjunction with Pinax starter
projects. If using the theme with Django < 1.4, you will need to install a recent
version of django-staticfiles as we use the `{% render %}` template tag.


Navigation
----------

To modify your site's navigation bar, implement the "nav" block in
your site_base.html using the following pattern: ::

    <ul class="nav navbar-nav">
        <li id="tab_first">
            <a href="#">First Link</a>
        </li>
        <li id="tab_second">
            <a href="#">Second Link</a>
        </li>
        <li id="tab_third" class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                Some Dropdown Menu
                <b class="caret"></b>
            </a>
            <ul class="dropdown-menu">
                <li><a href="#">Some Link</a></li>
                <li><a href="#">Another Link</a></li>
            </ul>
        </li>
    </ul>


Pagination
----------

This theme supports both django-pagination_ and Django builtin pagination.
See PaginationTemplate_ for information how to switch between them.


Roadmap
-------

The 2.x line of `pinax-theme-bootstrap` with support for Pinax 0.9 will soon
be phased out of major updates. We will be releasing a 3.x line that will
break backwards compatibility but fully support Pinax 1.0 projects. This
is a change towards a more semantic versioning strategy in lieu of merely
indicating which version of Bootstrap media is included. The 4.x line now
supports Bootstrap 3.0, while the 3.x line supports Bootstrap 2.x.


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

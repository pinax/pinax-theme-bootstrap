Twitter Bootstrap Theme, for Pinax
==================================

A theme for Pinax 0.9 based on Twitter's open source Bootstrap framework.


Quick Start
-----------

Include "pinax-theme-bootstrap" in your requirements file and include
"pinax_theme_bootstrap" and "django_forms_bootstrap" (which is installed alongside
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

- With newer versions of Bootstrap a light status bar is now default. If you'd like
  to use the darker navbar, simply override the `navbar_class` block in your
  site_base.html to something like the following (note we include the `fixed-top`
  class in this block by default, but it's also optional): ::

    {% block navbar_class %}navbar-inverse navbar-fixed-top{% endblock %}

- Base templates: To enable multiple themes to be used within a single site, base
  templates are now located under the "theme_bootstrap" folder. We will continue to
  provide base templates at the root path for backward compatibility, but these will
  likely be removed in a future version and you should update your site_base.html to
  extend from "theme_bootstrap/base.html".

- Forms Rendering: Versions prior to 2.0.3 included template tags for forms rendering.
  This has now been moved out to a new app, django-forms-bootstrap. You'll need to add
  this app to your `INSTALLED_APPS` as "django_forms_bootstrap".


Requirements
------------

This theme is officially supported when used in conjuction with Pinax 0.9.
If using the theme with Django < 1.4, you will need to install a recent
version of django-staticfiles as we use the `{% render %}` template tag.


Forms
-----

This theme makes use of django-forms-bootstrap for simple forms support.
Make sure you have the latest version of django-forms-bootstrap installed
in your virtualenv (if you install this theme with pip it will be installed
automatically) and add "django_forms_bootstrap" to your `INSTALLED_APPS`.

To style forms, add the following to the top of your template ::
    
    {% load bootstrap_tags %}

and include your form using something like the following markup: ::
    
    <form>
        <legend>My Form</legend>
        {% csrf_token %}
        {{ form|as_bootstrap }}
        <div class="form-actions">
          <a href="#back" class="btn">Go back</a>
          <button type="submit" class="btn btn-primary">Save changes</button>
        </div>
    </form>

Bootstrap includes styles for four types of forms. To change the display of
your form, add one of the following class attributes to your form tag:


==================  ================   ==============================================================
        Name             Class                        Description
==================  ================   ==============================================================
Vertical (default)  .form-vertical     Stacked, left-aligned labels over controls
Horizontal          .form-horizontal   Float left, right-aligned labels on same line as controls
Inline              .form-inline       Left-aligned label and inline-block controls for compact style
Search              .form-search       Extra-rounded text input for a typical search aesthetic
==================  ================   ==============================================================


Navigation
----------

To modify your site's navigation bar, implement the "nav" block in
your site_base.html using the following pattern: ::

    <ul class="nav">
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


Responsive Grid
---------------

Bootstrap's responsive grid makes designing layouts that work well on every
device a snap. We've included the the responsive stylesheet in this theme by
default. If you'd like to remove this from your site, include the following
two in your site_base.html: ::

    {# unset the viewport, telling mobile devices to scale your site #}
    {% block viewport %}{% endblock %}

    {# include all default stylesheets except the responsive grid #}
    {% block style_base %}
        <link href="{% static "pinax/css/theme.css" %}" rel="stylesheet">
        <link href="{% static "bootstrap/css/bootstrap.css" %}" rel="stylesheet">
        {% block extra_style %}{% endblock %}
    {% endblock %}

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
indicating which version of Bootstrap media is included.


License & Attribution
---------------------

The Pinax Bootstrap theme is released under the MIT license.

This theme includes styles and scripts from the Twitter Bootstrap project,
which is released under the Apache License, Version 2.0.

For copies of both licenses, see LICENSE.

Includes icons from `Glyphicons Free <http://glyphicons.com/>`_, licensed
under `CC BY 3.0 <http://creativecommons.org/licenses/by/3.0/>`_.

Includes icons from
`Font Awesome <http://fortawesome.github.io/Font-Awesome/>`_.


.. _PaginationTemplate: https://github.com/pinax/pinax-theme-bootstrap/blob/master/pinax_theme_bootstrap/templates/pagination/pagination.html
.. _django-pagination: https://github.com/ericflo/django-pagination

Twitter Bootstrap Theme, for Pinax
==================================

A theme for Pinax 0.9 based on Twitter's open source Bootstrap framework.


Quick Start
-----------

Include "pinax-theme-bootstrap" in your requirements file and
"pinax_theme_bootstrap" in your INSTALLED APPS.

Make sure both template loaders and staticfiles finders includes
app directories.

Site name comes from Sites fixture.

Your "site_base.html" should extend "theme_bootstrap/base.html" and should provide
"footer" and "nav" blocks (the latter should just be a ul of li of a links).

Your pages should have blocks "head_title" and "body" and should extend
"site_base.html".

The url name "home" should be defined as the homepage.


Requirements
------------

This theme is officially supported when used in conjuction with Pinax 0.9.
If using the theme with Django < 1.4, you will need to install a recent
version of django-staticfiles as we use the `{% render %}` template tag.


Forms
-----

This theme ships with a basic template tag for rendering forms that match
the markup expected by Bootstrap.

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


Upgrading from Bootstrap 1.x
----------------------------

Previous versions of this theme were based off of Bootstrap 1.x.
The following is a list of changes that you need to be aware of
when upgrading existing sites:

- The default grid has changed from 16 columns to 12 columns.
- Bootstrap 2 provides a responsive grid, which we've enabled by default.
- Forms markup has changed slightly, see the example above.
- Navigation bar markup now requires a class="nav" on the ul.


License & Attribution
---------------------

The Pinax Bootstrap theme is released under the MIT license.

This theme includes styles and scripts from the Twitter Bootstrap project,
which is released under the Apache License, Version 2.0.

For copies of both licenses, see LICENSE.

Includes icons from `Glyphicons Free <http://glyphicons.com/>`_, licensed
under `CC BY 3.0 <http://creativecommons.org/licenses/by/3.0/>`_.

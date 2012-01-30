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

Your "site_base.html" should extend "theme_base.html" and should provide
"footer" and "nav" blocks (the latter should just be a ul of li of a links).

Your pages should have blocks "head_title" and "body" and should extend
"site_base.html".

The url name "home" should be defined as the homepage.


Forms
-----


This theme ships with a basic template tag for rendering forms that match
the markup expected by Bootstrap.

To style forms, add the following to the top of your template ::
    
    {% load bootstrap_tags %}

and include your form using the following markup: ::
    
    <form method="POST" action="">
        {% csrf_token %}
        <fieldset class="form-controls">
            {{ form|as_bootstrap }}
        </fieldset>
        <fieldset class="form-actions">
            <button type="submit" class="btn primary">Submit</button>
        </fieldset>
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


Upgrading from Bootstrap 1.x
----------------------------

Previous versions of this theme were based off of Bootstrap 1.x.
The following is a list of changes that you need to be aware of
when upgrading existing sites:

- The default grid has changed from 16 columns to 12 columns.
- Bootstrap 2 provides a responsive grid, which we've enabled by default.
- Forms markup has changed slightly, see the example above.
- Navigation bar markup now requires a class="nav" on the ul.

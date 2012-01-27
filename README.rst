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

To style forms, 
    
    {% load bootstrap_tags %}

and do something like:
    
    <form method="POST" action="">
        {% csrf_token %}
        <fieldset class="form-controls">
            {{ form|as_bootstrap }}
        </fieldset>
        <fieldset class="form-actions">
            <button type="submit" class="btn primary">Submit</button>
        </fieldset>
    </form>


Navigation
----------

To modify your site's navigation bar, implement the "nav" block in
your site_base.html using the following pattern:

    <ul class="nav">
        <li><a href="#">First Link</a></li>
        <li><a href="#">Second Link</a></li>
    </ul>


Upgrading from Bootstrap 1.x
----------------------------

Previous versions of this theme were based off of Bootstrap 1.x.
The following is a list of changes that you need to be aware of
when upgrading existing sites:

- The default grid has changed from 16 columns to 12 columns.
- Forms markup has changed slightly, see the example above.
- Navigation bar markup now requires a class="nav" on the ul.

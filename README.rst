==================
django-privatebeta
==================

This reusable Django applications provides two things useful to a site under
private (closed) beta:

* A form that allows users to enter their email address so that you can send
  them an invite or a site launch notification later.
* A middleware that locks the site down for non-logged in users.  If you
  control account creation this is a very effective way of limiting a site
  to beta testers only.

Installation
============

Email invite form
-----------------

To use the invite form, you first need to add ``privatebeta`` to
``INSTALLED_APPS`` in your settings file::

    INSTALLED_APPS = (
    ...
    'privatebeta',
    )

You will also need to add ::

    urlpatterns = patterns('',
        ...
        (r'^invites/', include('privatebeta.urls')),
    )

You will also need to create two templates.  The first is
``privatebeta/invite.html``::

    {% extends 'base.html' %}

    {% block content %}
    <h3>Enter your email address and we'll send you an invite soon</h3>
    <form action="{% url privatebeta_invite %}" method="post">
    {{ form }}
    <input type="submit" value="Submit" />
    </form>
    {% endblock %}

When an email address is successfully entered, the user will be redirected to
``privatebeta/sent.html``::

    {% extends 'base.html' %}

    {% block content %}
    <p>Thanks, we'll be in touch!</p>
    {% endblock %}

The above templates assume a standard Django template structure with a
``base.html`` template and a ``content`` block.

The included views take two optional keyword arguments for flexibility.:

``template_name``
    The name of the tempalte to render.  Optional, overrides the default
    template.

``extra_context``
    A dictionary to add to the context of the view.  Keys will become
    variable names and values will be accessible via those variables.
    Optional.

Closed beta middleware
----------------------

If you would also like to prevent non-logged-in users from viewing your site,
you can make use of ``privatebeta.middleware.PrivateBetaMiddleware``.  This
middleware redirects all views to a specified location if a user is not logged in.

There are a few settings that influence behavior of the middleware:

``PRIVATEBETA_NEVER_ALLOW_VIEWS``
    A list of full view names that should *never* be displayed.  This
    list is checked before the others so that this middleware exhibits
    deny then allow behavior.

``PRIVATEBETA_ALWAYS_ALLOW_VIEWS``
    A list of full view names that should always pass through.

``PRIVATEBETA_ALWAYS_ALLOW_MODULES``
    A list of modules that should always pass through.  All
    views in ``django.contrib.auth.views``, ``django.views.static``
    and ``privatebeta.views`` will pass through unless they are
    explicitly prohibited in ``PRIVATEBETA_NEVER_ALLOW_VIEWS``

``PRIVATEBETA_REDIRECT_URL``
    The URL to redirect to.  Can be relative or absolute.

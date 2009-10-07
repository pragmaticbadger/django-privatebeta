from django.conf import settings
from django.http import HttpResponseRedirect

class PrivateBetaMiddleware(object):
    """
    Add this to your ``MIDDLEWARE_CLASSES`` make all views except for
    those in the account application require that a user be logged in.
    This can be a quick and easy way to restrict views on your site,
    particularly if you remove the ability to create accounts.
    
    **Settings:**
    
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
    """

    def __init__(self):
        self.never_allow_views = getattr(settings, 'PRIVATEBETA_NEVER_ALLOW_VIEWS', [])
        self.always_allow_views = getattr(settings, 'PRIVATEBETA_ALWAYS_ALLOW_VIEWS', [])
        self.always_allow_modules = getattr(settings, 'PRIVATEBETA_ALWAYS_ALLOW_MODULES', [])
        self.redirect_url = getattr(settings, 'PRIVATEBETA_REDIRECT_URL', '/invite/')

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated():
            # User is logged in, no need to check anything else.
            return
        whitelisted_modules = ['django.contrib.auth.views', 'django.views.static', 'privatebeta.views']
        if self.always_allow_modules:
            whitelisted_modules += self.always_allow_modules

        full_view_name = '%s.%s' % (view_func.__module__, view_func.__name__)

        if full_view_name in self.never_allow_views:
            return HttpResponseRedirect(self.redirect_url)

        if full_view_name in self.always_allow_views:
            return
        if '%s' % view_func.__module__ in whitelisted_modules:
            return
        else:
            return HttpResponseRedirect(self.redirect_url)

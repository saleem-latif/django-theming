"""
Module to contain all of the exceptions defined and used by the theming app.
"""
from __future__ import absolute_import

from django.core.exceptions import ImproperlyConfigured as DjangoImproperlyConfigured


class ThemeException(Exception):
    """
    Base exception for all theming related exceptions.
    """


class MiddlewareNotActivated(ThemeException):
    """
    Exception raised when features being used depends on a theming middleware.
    """


class ImproperlyConfigured(ThemeException, DjangoImproperlyConfigured):
    """
    Theming is somehow improperly configured.
    """

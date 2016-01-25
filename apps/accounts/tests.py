from __future__ import unicode_literals
from __future__ import absolute_import

from unittest import skipIf

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from django.test import TestCase, override_settings

import requests

from .oauth_backends.myoauth import MyOAuthOAuth2


def user_profile_undefined():
    """
    Helper function that returns true when MY_USER_PROFILE_URL
    setting is undefined or empty.
    """
    return not getattr(settings, 'MY_USER_PROFILE_URL', None)


class TestMyOAuthBackend(TestCase):
    @skipIf(user_profile_undefined(), "MY_USER_PROFILE_URL setting is empty or undefined")
    @override_settings(MY_USER_PROFILE_URL=None)
    def test_get_user_profile_url_raise_exception(self):
        backend = MyOAuthOAuth2()
        with self.assertRaises(ImproperlyConfigured):
            backend.get_user_profile_url()

    @skipIf(user_profile_undefined(), "MY_USER_PROFILE_URL setting is empty or undefined")
    def test_get_user_profile_url(self):
        url = MyOAuthOAuth2().get_user_profile_url()
        self.assertEqual(url, settings.MY_USER_PROFILE_URL)

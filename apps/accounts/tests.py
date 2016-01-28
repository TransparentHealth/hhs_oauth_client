from __future__ import unicode_literals
from __future__ import absolute_import

from unittest import skipIf

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from django.test import TestCase, override_settings

from .oauth_backends.myoauth import MyOAuthOAuth2


def user_profile_undefined():
    """
    Helper function that returns true when MY_USER_PROFILE_URL
    setting is undefined or empty.
    """
    return not getattr(settings, 'MY_USER_PROFILE_URL', None)


def no_test_server_credentials():
    """
    Helper function that returns true when TEST_INTEGRATION_*
    credentials are undefined or empty.
    """
    client_id = getattr(settings, 'TEST_INTEGRATION_CLIENT_ID', None)
    username = getattr(settings, 'TEST_INTEGRATION_USERNAME', None)
    password = getattr(settings, 'TEST_INTEGRATION_PASSWORD', None)
    return not (client_id and username and password)


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

    @skipIf(no_test_server_credentials(), "TEST_INTEGRATION_* setttings are empty or undefined")
    def test_user_data(self):
        """
        Tests that the server return a json with the expected schema and content.
        """
        # get a valid access token from the server
        access_token = self._get_test_access_token()
        # call oauth server to retrieve user data
        # the server should define an user with the following profile info
        from social.strategies.django_strategy import DjangoStrategy
        from social.storage.django_orm import BaseDjangoStorage
        user_data = MyOAuthOAuth2(DjangoStrategy(BaseDjangoStorage)).user_data(access_token)
        self.assertDictContainsSubset({
            'username': 'test_user',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test_user@a.com',
        }, user_data)

    def _get_test_access_token(self):
        """
        Helper method that returns an access token from the test server.
        """
        from oauthlib.oauth2 import LegacyApplicationClient
        from requests_oauthlib import OAuth2Session
        # get credentials for the test server
        client_id = getattr(settings, 'TEST_INTEGRATION_CLIENT_ID', None)
        username = getattr(settings, 'TEST_INTEGRATION_USERNAME', None)
        password = getattr(settings, 'TEST_INTEGRATION_PASSWORD', None)
        # get the access token with password flow
        oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
        token = oauth.fetch_token(
            token_url=settings.MY_ACCESS_TOKEN_URL,
            username=username, password=password, client_id=client_id)
        return token.get('access_token')

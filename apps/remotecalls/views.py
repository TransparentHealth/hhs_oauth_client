from __future__ import absolute_import
from __future__ import unicode_literals

import json

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

import requests
from requests_oauthlib import OAuth2


@login_required
def call_read(request):
    # first we get the token used to login
    token = request.user.social_auth.get(provider='myoauth').access_token
    auth = OAuth2(settings.SOCIAL_AUTH_MYOAUTH_KEY,
                  token={'access_token': token, 'token_type': 'Bearer'})
    # next we call the remote api
    url = urljoin(settings.HHS_OAUTH_URL, '/api/read/')
    response = requests.get(url, auth=auth)
    if response.status_code == 403:
        return JsonResponse({'error': 'no read capability'}, status=403)
    else:
        return JsonResponse(response.json(), status=response.status_code)


@login_required
@require_POST
def call_write(request):
    # first we get the token used to login
    token = request.user.social_auth.get(provider='myoauth').access_token
    auth = OAuth2(settings.SOCIAL_AUTH_MYOAUTH_KEY,
                  token={'access_token': token, 'token_type': 'Bearer'})
    # next we call the remote api
    url = urljoin(settings.HHS_OAUTH_URL, '/api/write/')
    response = requests.post(url, auth=auth, json=request.POST)
    if response.status_code == 403:
        return JsonResponse({'error': 'no write capability'}, status=403)
    else:
        return JsonResponse(response.json(), status=response.status_code)

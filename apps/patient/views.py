from __future__ import absolute_import
from __future__ import unicode_literals

import json

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_POST

import requests
from requests_oauthlib import OAuth2

@login_required
def bbof_pull_me(request):
    context = {'name': 'Blue Button on FHIR'}
    # first we get the token used to login
    token = request.user.social_auth.get(provider='myoauth').access_token
    auth = OAuth2(settings.SOCIAL_AUTH_MYOAUTH_KEY,
                  token={'access_token': token, 'token_type': 'Bearer'})
    # next we call the remote api
    url = urljoin(settings.HHS_OAUTH_URL, '/fhir/v3/oauth2/Patient/1')
    response = requests.get(url, auth=auth)

    
    if response.status_code == 200:
        content = response.json()
    elif response.status_code == 403:
        content = {'error': 'no read capability'}
    else:
        content = {'error': 'server error'}

    context['remote_status_code'] = response.status_code
    context['remote_content'] = content
    return render(request, 'bbof.html', context)



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
from django.contrib import messages
import requests
from requests_oauthlib import OAuth2
from .forms import JsonForm, PractitionerForm, OrganizationForm
from django.utils.translation import ugettext_lazy as _
from collections import OrderedDict


# Create your views here.

@login_required
def pjson_provider_push(request):
    context = {'name': 'Push PJSON Provider'}

    if request.method == 'POST':
        form = JsonForm(request.POST)
        if form.is_valid():
            # first we get the token used to login
            token = request.user.social_auth.get(provider=settings.PROPRIETARY_BACKEND_NAME).access_token
            auth = OAuth2(settings.SOCIAL_AUTH_MYOAUTH_KEY,
                          token={'access_token': token, 'token_type': 'Bearer'})
            # next we call the remote api
            url = urljoin(settings.HHS_OAUTH_URL, '/nppes/update')
            json_data = json.loads(form.cleaned_data['json'], object_pairs_hook=OrderedDict)
            response = requests.post(url, auth=auth, json=json_data)
            if response.status_code == 200:
                content = response.text#json()
            elif response.status_code == 403:
                content = {'error': 'no write capability'}
            else:
                content = {'error': 'server error'}
            context['remote_status_code'] = response.status_code
            context['remote_content'] = content
            return render(request, 'response.html', context)

        else:
            messages.error(request,_("Please correct the errors in the form."))
            return render( request, 'generic/bootstrapform.html',
                                            {'form': form})

    context['form'] = JsonForm()
    return render(request, 'generic/bootstrapform.html', context)


@login_required
def fhir_practitioner_push(request):
    context = {'name': 'Push FHIR Practitioner'}

    if request.method == 'POST':
        form = PractitionerForm(request.POST)
        if form.is_valid():
            # first we get the token used to login
            token = request.user.social_auth.get(provider=settings.PROPRIETARY_BACKEND_NAME).access_token
            auth = OAuth2(settings.SOCIAL_AUTH_MYOAUTH_KEY,
                          token={'access_token': token, 'token_type': 'Bearer'})
            # next we call the remote api

            json_data = json.loads(form.cleaned_data['json'], object_pairs_hook=OrderedDict)
            url = urljoin(settings.HHS_OAUTH_URL, '/fhir/v3/oauth2/Practitioner/%s') % (int(json_data['identifier'][0]['value']))

            response = requests.put(url, auth=auth, json=json_data)
            if response.status_code == 200:
                content = response.text#.json()
            elif response.status_code == 403:
                content = response.text #json()#{'error': 'no write capability'}
            else:
                content = response.text #json()#{'error': 'server error'}
            context['remote_status_code'] = response.status_code
            context['remote_content'] = content
            return render(request, 'response.html', context)

        else:
            messages.error(request,_("Please correct the errors in the form."))
            return render( request, 'generic/bootstrapform.html',
                                            {'form': form})

    context['form'] = PractitionerForm()
    return render(request, 'generic/bootstrapform.html', context)

@login_required
def fhir_organization_push(request):
    context = {'name': 'Push FHIR Organization'}

    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            # first we get the token used to login
            token = request.user.social_auth.get(provider=settings.PROPRIETARY_BACKEND_NAME).access_token
            auth = OAuth2(settings.SOCIAL_AUTH_MYOAUTH_KEY,
                          token={'access_token': token, 'token_type': 'Bearer'})
            # next we call the remote api

            json_data = json.loads(form.cleaned_data['json'], object_pairs_hook=OrderedDict)
            url = urljoin(settings.HHS_OAUTH_URL, '/fhir/v3/oauth2/Organization/%s') % (int(json_data['identifier'][0]['value']))

            response = requests.put(url, auth=auth, json=json_data)
            if response.status_code == 200:
                content = response.text#.json()
            elif response.status_code == 403:
                content = response.text #json()#{'error': 'no write capability'}
            else:
                content = response.text #json()#{'error': 'server error'}
            context['remote_status_code'] = response.status_code
            context['remote_content'] = content
            return render(request, 'response.html', context)

        else:
            messages.error(request,_("Please correct the errors in the form."))
            return render( request, 'generic/bootstrapform.html',
                                            {'form': form})

    context['form'] = OrganizationForm()
    return render(request, 'generic/bootstrapform.html', context)

from __future__ import absolute_import
from __future__ import unicode_literals

import json

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
import requests
from requests_oauthlib import OAuth2
from .forms import (JsonForm, PractitionerForm, OrganizationForm,
                    FetchPractitionerForm, PractitionerHumanForm,
                    PractitionerModelForm, AddressForm)
from django.utils.translation import ugettext_lazy as _
from collections import OrderedDict
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .utils import get_practitioner, convert_practioner_fhir_to_form
from .models import Practitioner, Address
import json

@login_required
def fetch_practitioner(request):
    context = {'name': 'Enter Your NPI'}
    if request.method == 'POST':
        form = FetchPractitionerForm(request.POST)
        if form.is_valid():
            npi = form.cleaned_data.get('npi')
            
            return HttpResponseRedirect(reverse('update_practitioner',
                            args=(npi,)))
        else:
            messages.error(request,_("Please correct the errors in the form."))
            return render( request, 'generic/bootstrapform.html',
                                            {'form': form})       
            
    context['form'] = FetchPractitionerForm()
    return render(request, 'generic/bootstrapform.html', context)


@login_required
def submit_to_fhir(request, npi):
    p = get_object_or_404(Practitioner, npi=npi)
    
    
    print(p.to_fhir_json())
    messages.success(request,_("Practitioner updates submitted to the central provider directory"))
    return HttpResponseRedirect(reverse('update_practitioner', args=(npi,)))


    
@login_required
def update_practitioner(request, npi):
    context = {'name': 'Update Base Record for Practitioner %s' % (npi),
               'npi':npi}
    if request.method == 'POST':
        p = Practitioner.objects.get(npi=npi)
        form = PractitionerModelForm(request.POST, instance=p)     
        if form.is_valid():
            form.save()
            messages.success(request,_("Practitioner updated."))
            return HttpResponseRedirect(reverse('update_practitioner',
                            args=(npi,)))

        else:
            messages.error(request,_("Please correct the errors in the form."))
            context['form'] = form
            return render( request, 'practitioner-form.html', context)       
            
    #This is an HTTP GET so do a fetch
    pract_res =  get_practitioner(npi)
    #print(json.dumps(pract_res, indent =4))
    
    data = convert_practioner_fhir_to_form(pract_res, request.user)
    
    p, get_or_create = Practitioner.objects.get_or_create(**data)
    #Delete old addresses (if any) when this is a create
    if get_or_create:
        Address.objects.filter(npi=npi).delete()
        #Add new addresses
        for a in pract_res['address']:
            Address.objects.create(npi=npi, fhir_json_snipit=json.dumps(a, indent=4))
    
    context['form'] = PractitionerModelForm(instance=p)
    context['addresses'] = Address.objects.filter(npi=npi)
    return render(request, 'practitioner-form.html', context)


@login_required
def create_address(request, npi):
    context = {'name': 'Update Address'}
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            Address.objects.create(fhir_json_snipit=form.create_fhir_json(),npi=npi)
            messages.success(request,_("Address Added"))
            return HttpResponseRedirect(reverse('update_practitioner',
                            args=(npi,)))
        else:
            messages.error(request,_("Please correct the errors in the form."))
            return render( request, 'generic/bootstrapform.html',
                                            {'form': form})       
            
    context['form'] = AddressForm()
    return render(request, 'generic/bootstrapform.html', context)

@login_required
def delete_address(request, id):
    a = get_object_or_404(Address, id=id)
    a.delete()
    messages.success(request,_("Address Deleted"))
    return HttpResponseRedirect(reverse('update_practitioner',
                            args=(a.npi,)))


@login_required
def update_address(request, id):
    
    a = get_object_or_404(Address, id=id)
    context = {'name': 'Update Address'}
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            a.fhir_json_snipit=form.create_fhir_json()
            a.save()
            messages.success(request,_("Address Updated"))
            return HttpResponseRedirect(reverse('update_practitioner',
                            args=(a.npi,)))
        else:
            messages.error(request,_("Please correct the errors in the form."))
            return render( request, 'generic/bootstrapform.html',
                                            {'form': form})       
            
    context['form'] = AddressForm(initial=a.as_dict())
    return render(request, 'generic/bootstrapform.html', context)



    

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
def fhir_practitioner_update(request):
    context = {'name': 'Update FHIR Practitioner'}

    if request.method == 'POST':
        form = PractitionerForm(request.POST)
        if form.is_valid():
            # first we get the token used to login
            token = request.user.social_auth.get(provider=settings.PROPRIETARY_BACKEND_NAME).access_token
            auth = OAuth2(settings.SOCIAL_AUTH_MYOAUTH_KEY,
                          token={'access_token': token, 'token_type': 'Bearer'})
            # next we call the remote api

            json_data = json.loads(form.cleaned_data['json'], object_pairs_hook=OrderedDict)
            url = urljoin(settings.HHS_OAUTH_URL, '/fhir/v3/oauth2/Practitioner/%s') % (json_data['id'])

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
def fhir_organization_update(request):
    context = {'name': 'Update FHIR Organization'}

    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            # first we get the token used to login
            token = request.user.social_auth.get(provider=settings.PROPRIETARY_BACKEND_NAME).access_token
            auth = OAuth2(settings.SOCIAL_AUTH_MYOAUTH_KEY,
                          token={'access_token': token, 'token_type': 'Bearer'})
            # next we call the remote api

            json_data = json.loads(form.cleaned_data['json'], object_pairs_hook=OrderedDict)
            url = urljoin(settings.HHS_OAUTH_URL, '/fhir/v3/oauth2/Organization/%s') % (json_data['id'])

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
            url = urljoin(settings.HHS_OAUTH_URL, '/fhir/v3/oauth2/Practitioner')

            response = requests.post(url, auth=auth, json=json_data)
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
            url = urljoin(settings.HHS_OAUTH_URL, '/fhir/v3/oauth2/Organization')

            response = requests.post(url, auth=auth, json=json_data)
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

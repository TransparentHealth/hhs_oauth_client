from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from .views import *


urlpatterns = patterns('',
    url(r'^pjson/push$', pjson_provider_push,  name="pjson_provider_push"),
    url(r'^fhir/practitioner/push$', fhir_practitioner_push,  name="fhir_practitioner_push"),
    url(r'^fhir/organization/push$', fhir_organization_push,  name="fhir_organization_push"),
    url(r'^fhir/practitioner/update$', fhir_practitioner_update,  name="fhir_practitioner_update"),
    url(r'^fhir/organization/update$', fhir_organization_update,  name="fhir_organization_update"),

)

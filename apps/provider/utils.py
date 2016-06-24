import requests
import json

def get_practitioner(npi):
    """Returns a Practitioner Resource from Djmongo"""
    url = "https://registry.npi.io/search/fhir/Practitioner.json?identifier.value=%s" % (npi)
    response = requests.get(url)
    try:
        jr = json.loads(response.text)
        
        if 'results' not in jr:
            jr = {'error', 'The lookup failed. Invalid response from server'}
        
        if not jr['results']:
                jr = {'error', 'Invalid NPI'}
    except ValueError:
        jr = {'error', 'The lookup failed. JSON was not returned from the server.'} 
    
    return jr['results'][0]

def convert_practioner_fhir_to_form(pract_res, user):
    """Converts a Practitioner Resource into Values for Form"""
    data = {}
    data['user'] = user
    data['first_name']= pract_res['name'][0]['given'][0]
    data['last_name']= pract_res['name'][0]['family'][0]
    data['npi']= pract_res['identifier'][0]['value']
    data['fhir_id']= pract_res['id']
    
    
    return data


def convert_practioner_fhir_to_meta(pract_res, user):
    """Converts a Practitioner Resource into Values for Form"""
    data = {}
    data['user'] = user
    data['npi']= pract_res['identifier'][0]['value']
    data['fhir_id']= pract_res['id']
    
    
    return data
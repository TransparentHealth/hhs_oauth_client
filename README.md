HHS oAuth Client  - An oAuth Provider Sample Project
================================================

## Quick Setup

    git clone https://github.com/videntity/hhs_oauth_client.git
    pip install -r oauth_provider/requirements.txt
    python manage.py syncdb
    python manage.py runserver

## Running the tests

To run the tests against http://oauth.npi.io/ use:

    python manage.py test --settings=hhs_oauth_client.settings.test

To run the tests against a local server instance (http://127.0.0.1:8000) use:

    python manage.py test --settings=hhs_oauth_client.settings.test_local

N.B. Remember to launch ``python manage.py load_test_data`` on the server instance
to create test users, apps and capabilities.

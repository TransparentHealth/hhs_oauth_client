HHS oAuth Client  - An oAuth Provider Sample Project
================================================

## Quick Setup

    git clone https://github.com/videntity/hhs_oauth_client.git
    pip install -r oauth_provider/requirements.txt
    python manage.py syncdb
    python manage.py runserver

## Running the tests

    python manage.py test --settings=hhs_oauth_client.settings.test

from .base import *

SECRET_KEY = "HHSCLIENT-LOCAL-_cdlv24!g$4)b&wq9fjn)p!vrs729idssk2qp7iy!u#"

DBPATH=os.path.join(BASE_DIR, 'db/db.db')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DBPATH,                   # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SOCIAL_AUTH_MYOAUTH_KEY = 'RoxnbCWTyU48yCmx0dHaHfnhWRNgsQT1y9GNbLV5'
SOCIAL_AUTH_MYOAUTH_SECRET = 'xdXCY5C5wADrQyHUj6j9NataYt48U3KCzF5Nuk1vHWDe0JtFS9On5w8nsj68GYb3Gbm2bljB9jG98RC3oto5wbg02Dbr3RtRdPd5JqtOsrykPTVDIR7QJOWkuFNutXMv'
SOCIAL_AUTH_MYOAUTH_EXTRA_ARGUMENTS = {'scope': 'blue-button-read-only provider-data-push'}
HHS_OAUTH_URL = "http://oauth:8000"
MY_AUTHORIZATION_URL = ('%s/o/authorize/') % (HHS_OAUTH_URL)
MY_ACCESS_TOKEN_URL =  '%s/o/token/' % (HHS_OAUTH_URL)
MY_USER_PROFILE_URL =  '%s/api/profile/' % (HHS_OAUTH_URL)
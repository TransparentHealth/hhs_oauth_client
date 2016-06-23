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

SOCIAL_AUTH_MYOAUTH_KEY = 'KKZ0l21ZvikhYhx9BhTGsCHOy8I0iZN0SIsBQYRW'
SOCIAL_AUTH_MYOAUTH_SECRET = 'E5EptnKD3LRCarzTRP39UsT9afqRHcGn4uId0hCWx7Z9KCe4F7vWfsTJAO1EpZkbBaQamxiOLaCN8jf5b8Vz1079VY6F27Ps6qRI4SefgRP7RDgVVXkaQ8OmMBZwg0al'
SOCIAL_AUTH_MYOAUTH_EXTRA_ARGUMENTS = {'scope': 'blue-button-read-only provider-data-push'}
HHS_OAUTH_URL = "http://oauth:8000"
MY_AUTHORIZATION_URL = ('%s/o/authorize/') % (HHS_OAUTH_URL)
MY_ACCESS_TOKEN_URL =  '%s/o/token/' % (HHS_OAUTH_URL)
MY_USER_PROFILE_URL =  '%s/profile/me' % (HHS_OAUTH_URL)

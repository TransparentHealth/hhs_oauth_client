from .settings import *

SOCIAL_AUTH_MYOAUTH_KEY = 'ucTySDRajnv9jaUss5VRxnOUJQOKTqeZ7olDdWRn'
SOCIAL_AUTH_MYOAUTH_SECRET = 'rnWHw51aHluNuu1ZLiRDNdUAOjeGfLpzWpdySbcQu4v3KXwDnzBpg18GYv0V5SAmgz2bmUGjYmHGJzxzN5eU0pXQLDB6gJSX8WoaiGHdJPDi9hP5YYL6YsQg0tp0rkNm'
# the trailing slash is necessary, because python-social-auth does not follow
# redirects by default.
#HHS_OAUTH_URL = "http://oauth:8000"
HHS_OAUTH_URL = "http://bluefitbutton.ekivemark.com:8000"

MY_AUTHORIZATION_URL = ('%s/o/authorize/') % (HHS_OAUTH_URL)
MY_ACCESS_TOKEN_URL =  '%s/o/token/' % (HHS_OAUTH_URL)
MY_USER_PROFILE_URL =  '%s/api/profile/' % (HHS_OAUTH_URL)

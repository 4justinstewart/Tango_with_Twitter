import requests
import os
import socket
import urllib
from django.http import HttpRequest
# from requests_oauthlib import OAuth1 (NOT INSTALLED ON MACHINE)


class OAuth:

    def request_oauthtoken(self, request):
        # location = request.get_full_path()
        # full = request.build_absolute_uri()
        
        host = request.META['HTTP_HOST']
        domain = 'http://%s/deals/oauth' % (host)
        encoded_callback = urllib.quote_plus(domain)

        payload = { 'oauth_callback': encoded_callback }
        return payload

        # r = requests.get('https://api.twitter.com/oauth/request_token', params=payload)

        # print(r.text)

    def access_headers(self):
        return { 
            'oauth_consumer_key' : os.environ('API_KEY'), 
            'oauth_nonce' : os.environ('API_SECRET'), 
            'oauth_signature' : '',
            'oauth_signature_method' : 'HMAC-SHA1',
            'oauth_timestamp' : 'number of seconds since Unix epoch?',
            'oauth_token' : '', # needs to be requested
            'oauth_version' : '1.0'
          }

    def token_headers(self, callback_url):
        return { 
            'oauth_callback' : callback_url,
            'oauth_consumer_key' : os.environ('API_KEY'),
            'oauth_nonce' : os.environ('API_SECRET'),
            'oauth_signature' : '',
            'oauth_signature_method' : 'HMAC-SHA1',
            'oauth_timestamp' : 'number of seconds since Unix epoch?',
            'oauth_version' : '1.0'
          }


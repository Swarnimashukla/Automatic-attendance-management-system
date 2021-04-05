import sys
import os, time
import cognitive_face as CF
import global_variables as global_var
import urllib
import sqlite3
import requests
from urllib3.exceptions import InsecureRequestWarning

from global_variables import personGroupId
#from . import  util

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


Key = global_var.key

CF.Key.set(Key)

DEFAULT_BASE_URL = global_var.BASE_URL  # Replace with your regional Base URL
CF.BaseUrl.set(DEFAULT_BASE_URL)


#DEFAULT_BASE_URL = os.environ['FACE_ENDPOINT']

TIME_SLEEP = 1

class CognitiveFaceException(Exception):
    """Custom Exception for the python SDK of the Cognitive Face API.
    Attributes:
        status_code: HTTP response status code.
        code: error code.
        msg: error message.
    """

    def __init__(self, status_code, code, msg):
        super(CognitiveFaceException, self).__init__()
        self.status_code = status_code
        self.code = code
        self.msg = msg

    def __str__(self):
        return ('Error when calling Cognitive Face API:\n'
                '\tstatus_code: {}\n'
                '\tcode: {}\n'
                '\tmessage: {}\n').format(self.status_code, self.code,
                                          self.msg)

class BaseUrl(object):
    @classmethod
    def set(cls, base_url):
        if not base_url.endswith('/'):
            base_url += '/'
        cls.base_url = base_url

    @classmethod
    def get(cls):
        if not hasattr(cls, 'base_url') or not cls.base_url:
            cls.base_url = DEFAULT_BASE_URL
        return cls.base_url

class Key(object):
    """Manage Subscription Key."""

    @classmethod
    def set(cls, key):
        """Set the Subscription Key."""
        cls.key = key

    @classmethod
    def get(cls):
        """Get the Subscription Key."""
        if not hasattr(cls, 'key'):
            cls.key = None
        return cls.key

def request(method, url, data=None, json=None, headers=None, params=None):
    # pylint: disable=too-many-arguments
    """Universal interface for request."""

    # Make it possible to call only with short name (without BaseUrl).
    if not url.startswith('https://'):
        url = BaseUrl.get() + url

    # Setup the headers with default Content-Type and Subscription Key.
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    headers['Ocp-Apim-Subscription-Key'] = global_var.key
    print()

    response = requests.request(
        method,
        url,
        params=params,
        data=data,
        json=json,
        headers=headers)

    # Handle result and raise custom exception when something wrong.
    result = None
    # `person_group.train` return 202 status code for success.
    if response.status_code not in (200, 202):
        try:
            error_msg = response.json()['error']
        except:
            raise CognitiveFaceException(response.status_code,
                                         response.status_code, response.text)
        raise CognitiveFaceException(response.status_code,
                                     error_msg.get('code'),
                                     error_msg.get('message'))

    # Prevent `response.json()` complains about empty response.
    if response.text:
        result = response.json()
    else:
        result = {}

    return result

def delete(person_group_id):
    """Delete an existing person group. Persisted face images of all people in
    the person group will also be deleted.
    Args:
        person_group_id: The `person_group_id` of the person group to be
            deleted.
    Returns:
        An empty response body.
    """
    url = 'persongroups/{}'.format(person_group_id)

    return request('DELETE', url)


delete(personGroupId)
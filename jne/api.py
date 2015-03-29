# -*- coding: utf-8 -*-

"""
jne.api
~~~~~~~~~~~
This module contains functionality for access to JNE API calls,
and miscellaneous methods that are useful when dealing with the JNE API
"""

import json

import requests
from requests.exceptions import RequestException

from .constants import (URL_CITY_FROM, URL_CITY_TO, URL_TARIFF, URL_TRACKING,
                        URL_NEARBY)
from .exceptions import JneAPIError
from .utils import pretty_print as pprint


class Jne(object):
    def __init__(self, api_key=None, username=None):
        """Instantiates an instance of Jne. Takes optional parameters for
        authentication (see below).
        :param api_key: Your api key from JNE
        :param username: Your username from JNE
        """
        self.api_key = api_key
        self.username = username

    def _request(self, api_call, method='GET', data={}, params={}):
        """Internal request method"""
        method = method.upper()
        payload = {'api_key': self.api_key, 'username': self.username}

        try:
            if method == 'GET':
                params.update(payload)
                response = requests.get(api_call, params=params)
            elif method == 'POST':
                data.update(payload)
                response = requests.post(api_call, params=params, data=data)
            else:
                raise ValueError("Method '{}' is not supported".format(method))
        except RequestException as error:
            raise JneAPIError(error)
        return json.loads(response.text)

    def get_from_code(self, city, pretty_print=False):
        """Return dict of JNE origin city code
        :param city: (required) Name of city that you want to know the code
        :param pretty_print: (optional True or False) To print the result
                             becomes more readable
        """
        response = self._request(method='POST',
                                 api_call=URL_CITY_FROM + city)
        if pretty_print:
            return pprint(response)
        return response

    def get_target_code(self, city, pretty_print=False):
        """Return dict of JNE destination city code
        :param city: (required) Name of city that you want to know the code
        :param pretty_print: (optional True or False) To print the result
                             becomes more readable
        """
        response = self._request(method='POST', api_call=URL_CITY_TO,
                                 params={'term': city})
        if pretty_print:
            return pprint(response)
        return response

    def check_tariff(self, city_from, city_to, weight=1, pretty_print=False):
        """return dict of JNE tariff
        :param city_from: (required) Origin city code. Ex: "CGK10000"
        :param city_to: (required) Target city code. Ex: "CBN10000"
        :param weight: (required) Weight of item.
        :param pretty_print: (optional True or False) To print the result
                             becomes more readable
        """
        data = {'from': city_from, 'thru': city_to, 'weight': weight}
        response = self._request(method='POST', api_call=URL_TARIFF,
                                 data=data)
        if pretty_print:
            return pprint(response)
        return response

    def tracking(self, airbill, pretty_print=False):
        """Return dict of JNE tracking detail
        :param airbill: (required) Airbill number from JNE
        :param pretty_print: (optional True or False) To print the result
                             becomes more readable
        """
        response = self._request(method='POST', api_call=URL_TRACKING + airbill)
        if pretty_print:
            return pprint(response)
        return response

    def find_nearby(self, latitude, longitude, pretty_print=False):
        """Return dict of JNE nearby based latitude and longitude
        :param latitude: (required) Latitude
        :param longitude: (required) Longitude
        :param pretty_print: (optional True or False) To print the result
                             becomes more readable
        """
        data = {'latitude': latitude, 'longitude': longitude}
        response = self._request(method='POST', api_call=URL_NEARBY, data=data)
        if pretty_print:
            return pprint(response)
        return response

import json

import requests
from requests.exceptions import RequestException

from .constants import URL_CITY_FROM, URL_CITY_TO, URL_TARIFF, URL_TRACKING
from .exceptions import JneAPIError
from .utils import pretty_print as pprint


class Jne(object):
    def __init__(self, api_key=None, username=None):
        self.api_key = api_key
        self.username = username

    def _request(self, api_call, method='GET', data={}, params={}):
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
        response = self._request(method='POST',
                                 api_call=URL_CITY_FROM + city)
        if pretty_print:
            return pprint(response)
        return response

    def get_target_code(self, city, pretty_print=False):
        response = self._request(method='POST', api_call=URL_CITY_TO,
                                 params={'term': city})
        if pretty_print:
            return pprint(response)
        return response

    def check_tariff(self, city_from, city_to, weight=1, pretty_print=False):
        data = {'from': city_from, 'thru': city_to, 'weight': weight}
        response = self._request(method='POST', api_call=URL_TARIFF,
                                 data=data)
        if pretty_print:
            return pprint(response)
        return response

    def tracking(self, airbill, pretty_print=False):
        response = self._request(method='POST', api_call=URL_TRACKING + airbill)
        if pretty_print:
            return pprint(response)
        return response

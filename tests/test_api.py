import json
import responses
import unittest

from jne import Jne
from jne.constants import (URL_TRACKING, URL_TARIFF, URL_CITY_FROM, URL_CITY_TO,
                           URL_NEARBY)


class JneAPITest(unittest.TestCase):

    def setUp(self):
        self.api = Jne(api_key='25c898a9faea1a100859ecd9ef6745487',
                       username='TESTAPI')

    def register_response(self, method, url, body='{}', match_querystring=False,
                          status=200, adding_headers=None, stream=False,
                          content_type='application/json; charset=utf-8'):

        responses.add(method, url, body, match_querystring,
                      status, adding_headers, stream, content_type)

    @responses.activate
    def test_tracking(self):
        response_body = {
            "cnote": {
                "city_name": "CIREBON",
            },
            "detail": [{
                "cnote_destination": "CIREBON",
                "cnote_no": "0113101501682546",
            }]
        }

        airbill = "0113101501682546"
        self.register_response(responses.POST, URL_TRACKING + airbill,
                               body=json.dumps(response_body))

        response = self.api.tracking(airbill=airbill)
        self.assertEqual(response['cnote']['city_name'], 'CIREBON')
        self.assertEqual(response['detail'][0]['cnote_destination'], 'CIREBON')
        self.assertEqual(response['detail'][0]['cnote_no'], '0113101501682546')

    @responses.activate
    def test_check_tariff(self):
        response_body = {
            "price": [{
                "destination_name": "CIREBON",
                "etd_from": "2",
                "etd_thru": "3",
                "origin_name": "JAKARTA",
                "price": "9000",
                "service_code": "OKE13",
                "service_display": "OKE",
                "times": "D"
            }, {
                "destination_name": "CIREBON",
                "etd_from": "1",
                "etd_thru": "2",
                "origin_name": "JAKARTA",
                "price": "10000",
                "service_code": "REG13",
                "service_display": "REG",
                "times": "D"
            }, {
                "destination_name": "CIREBON",
                "etd_from": None,
                "etd_thru": None,
                "origin_name": "JAKARTA",
                "price": "350000",
                "service_code": "SPS13",
                "service_display": "SPS",
                "times": None
            }, {
                "destination_name": "CIREBON",
                "etd_from": "1",
                "etd_thru": None,
                "origin_name": "JAKARTA",
                "price": "19000",
                "service_code": "YES13",
                "service_display": "YES",
                "times": "D"
            }]
        }

        self.register_response(responses.POST, URL_TARIFF,
                               body=json.dumps(response_body))

        response = self.api.check_tariff(city_from='CGK10000', city_to='CBN10000')

        self.assertEqual(response['price'][0]['destination_name'], 'CIREBON')
        self.assertEqual(response['price'][0]['origin_name'], 'JAKARTA')
        self.assertEqual(response['price'][0]['price'], '9000')

    @responses.activate
    def test_get_from_code(self):
        response_body = {
            "detail": [
                {
                    "code": "CGK10000",
                    "label": "JAKARTA"
                }
            ]
        }

        self.register_response(responses.POST, URL_CITY_FROM + 'jakarta',
                               body=json.dumps(response_body))

        response = self.api.get_from_code('jakarta')

        self.assertEqual(response['detail'][0]['code'], 'CGK10000')
        self.assertEqual(response['detail'][0]['label'], 'JAKARTA')

    @responses.activate
    def test_get_target_code(self):
        response_body = {
            'detail': [
                {
                    "code": "CGK10000",
                    "label": "JAKARTA"
                }, {
                    "code": "CGK10100",
                    "label": "JAKARTA BARAT"
                }, {
                    "code": "CGK10300",
                    "label": "JAKARTA PUSAT"
                }, {
                    "code": "CGK10200",
                    "label": "JAKARTA SELATAN"
                }, {
                    "code": "CGK10500",
                    "label": "JAKARTA TIMUR"
                }, {
                    "code": "CGK10400",
                    "label": "JAKARTA UTARA"
                }
            ]
        }

        self.register_response(responses.POST, URL_CITY_TO + '?term=jakarta',
                               body=json.dumps(response_body),
                               match_querystring={'term': 'jakarta'})

        response = self.api.get_target_code('jakarta')

        self.assertEqual(response['detail'][0]['code'], 'CGK10000')
        self.assertEqual(response['detail'][0]['label'], 'JAKARTA')
        self.assertEqual(response['detail'][1]['code'], 'CGK10100')
        self.assertEqual(response['detail'][1]['label'], 'JAKARTA BARAT')
        self.assertEqual(response['detail'][2]['code'], 'CGK10300')
        self.assertEqual(response['detail'][2]['label'], 'JAKARTA PUSAT')

    @responses.activate
    def test_find_nearby(self):
        # Mock API response
        response_body = {
            "places": [
                {
                    "custaddr1": "JL CIKINI RAYA NO40 MENTENG JAKARTA PUSAT",
                    "custaddr2": None,
                    "custname": "JNE ASP SEVEL CIKINI",
                    "jarak": "     0.10",
                    "latitude": "-6.19164",
                    "longitude": "106.8385"
                }, {
                    "custaddr1": "JL KWITANG RAYA NO 19-20 JAKARTA PUSAT",
                    "custaddr2": None,
                    "custname": "JNE AGEN 0200033",
                    "jarak": "     0.26",
                    "latitude": "-6.1808",
                    "longitude": "106.8392"
                }
            ]
        }

        self.register_response(responses.POST, URL_NEARBY,
                               body=json.dumps(response_body))

        response = self.api.find_nearby(latitude='-6.1886183', longitude='106.8387325')

        self.assertEqual(response['places'][0]['custname'], 'JNE ASP SEVEL CIKINI')
        self.assertEqual(response['places'][0]['jarak'].strip(), '0.10')
        self.assertEqual(response['places'][1]['custname'], 'JNE AGEN 0200033')
        self.assertEqual(response['places'][1]['jarak'].strip(), '0.26')

PyJNE
=====

PyJNE is a tool to simplify the user in using the API JNE such as tracking stuff, check tariffs and others.



Features
--------

- Get origin city code
- Get destination city code
- Check JNE tariffs
- Tracking stuff
- Find Nearby


Installation
------------

Install PyJNE via [pip](http://www.pip-installer.org/)

```bash
$ pip install py-jne
```



Usage
-----

#### 1. Get origin city code
---
```python
>>> from jne import Jne
>>> jne = Jne(api_key='d4dedbecf40d6d09f22704342c07d804', username='TESTAPI')
>>> jne.get_from_code('jakarta')
{u'detail': [{u'code': u'CGK10000', u'label': u'JAKARTA'}]}
>>>
>>> # Show result with pretty print
>>> jne.get_from_code('jakarta', pretty_print=True)
{
  "detail": [
    {
      "code": "CGK10000",
      "label": "JAKARTA"
    }
  ]
}
>>>
```

#### 2. Get destination city code
---
```python
>>> jne.get_target_code('jakarta')
[{u'code': u'CGK10000', u'label': u'JAKARTA'}, {u'code': u'CGK10100', u'label': u'JAKARTA BARAT'}, {u'code': u'CGK10300', u'label': u'JAKARTA PUSAT'}, {u'code': u'CGK10200', u'label': u'JAKARTA SELATAN'}, {u'code': u'CGK10500', u'label': u'JAKARTA TIMUR'}, {u'code': u'CGK10400', u'label': u'JAKARTA UTARA'}]
>>>
>>> # Show result with pretty print
>>> jne.get_target_code('Cirebon', pretty_print=True)
[
  {
    "code": "CBN10000",
    "label": "CIREBON"
  },
  {
    "code": "CBN10006",
    "label": "CIREBON BARAT,CIREBON"
  },
  {
    "code": "CBN20408",
    "label": "CIREBON SELATAN, SUMBER"
  },
  {
    "code": "CBN20407",
    "label": "CIREBON UTARA, SUMBER"
  }
]
>>>
```

#### 3. Check tariff
---
```python
>>> jne.check_tariff(city_from='CGK10000', city_to='CBN10000', weight=1)
{u'price': [{u'service_code': u'OKE13', u'etd_from': u'2', u'price': u'9000', u'origin_name': u'JAKARTA', u'times': u'D', u'service_display': u'OKE', u'etd_thru': u'3', u'destination_name': u'CIREBON'}, {u'service_code': u'REG13', u'etd_from': u'1', u'price': u'10000', u'origin_name': u'JAKARTA', u'times': u'D', u'service_display': u'REG', u'etd_thru': u'2', u'destination_name': u'CIREBON'}, {u'service_code': u'SPS13', u'etd_from': None, u'price': u'350000', u'origin_name': u'JAKARTA', u'times': None, u'service_display': u'SPS', u'etd_thru': None, u'destination_name': u'CIREBON'}, {u'service_code': u'YES13', u'etd_from': u'1', u'price': u'19000', u'origin_name': u'JAKARTA', u'times': u'D', u'service_display': u'YES', u'etd_thru': None, u'destination_name': u'CIREBON'}]}
>>>
>>>
>>> # Show result with pretty print
>>> jne.check_tariff(city_from='CGK10000', city_to='CBN10000', weight=1, pretty_print=True)
{
  "price": [
    {
      "destination_name": "CIREBON",
      "etd_from": "2",
      "etd_thru": "3",
      "origin_name": "JAKARTA",
      "price": "9000",
      "service_code": "OKE13",
      "service_display": "OKE",
      "times": "D"
    },
    {
      "destination_name": "CIREBON",
      "etd_from": "1",
      "etd_thru": "2",
      "origin_name": "JAKARTA",
      "price": "10000",
      "service_code": "REG13",
      "service_display": "REG",
      "times": "D"
    },
    {
      "destination_name": "CIREBON",
      "etd_from": null,
      "etd_thru": null,
      "origin_name": "JAKARTA",
      "price": "350000",
      "service_code": "SPS13",
      "service_display": "SPS",
      "times": null
    },
    {
      "destination_name": "CIREBON",
      "etd_from": "1",
      "etd_thru": null,
      "origin_name": "JAKARTA",
      "price": "19000",
      "service_code": "YES13",
      "service_display": "YES",
      "times": "D"
    }
  ]
}
>>>
```

#### 4. Tracking
---
```python
>>> jne.tracking(airbill='0113101501682546')
{u'runsheet': [{u'city_name': u'TANGERANG', u'pod_status': u'ON PROCESS', u'drsheet_cnote_no': u'0113101501682546', u'mrsheet_date': u'18-mar-2015 09:55'}], u'ip': u'192.168.2.228', u'detail': [{u'cnote_date': u'14-03-2015 01:29', u'cnote_destination': u'KOSAMBI / SELEMBARAN JATI', u'cnote_shipper_addr3': None, u'cnote_origin': u'JAKARTA', u'cnote_shipper_addr1': u'PUNINAR LOGISTIC JL INSPEKSI', u'cnote_shipper_addr2': u'KIRANA NAGRAK CAKUNG DRAIN', u'cnote_shipper_name': u'LAZADA (ECART WEBPORTAL IND)', u'cnote_receiver_addr3': u' NO. 4 RT 004 / 004 JL. RAYA D', u'cnote_receiver_addr2': u'004 / 004 JL. RAYA DADAP SAWAH', u'cnote_receiver_addr1': u'JL. RAYA DADAP SAWAH NO. 4 RT', u'cnote_shipper_city': u'JAKARTA UTARA', u'cnote_receiver_city': u'KOSAMBI / SELEMBARAN', u'cnote_weight': u'1', u'cnote_no': u'0113101501682546', u'cnote_receiver_name': u'UDI TUKANG IKAN'}], u'cnote': {u'cnote_date': u'2015-03-14', u'cnote_receiver_name': u'UDI TUKANG IKAN', u'cnote_pod_receiver': u'UDIN', u'cnote_pod_date': u'18 Mar 2015  13:00', u'pod_status': u'DELIVERED', u'cnote_services_code': u'REG', u'city_name': u'KOSAMBI / SELEMBARAN JATI', u'cnote_no': u'0113101501682546'}, u'manifest': [{u'mfcnote_no': u'0113101501682546', u'city_name': u'JAKARTA', u'manifest_date': u'14-MAR-2015 03:24', u'manifest_code': u'1', u'keterangan': u'Manifested'}, {u'mfcnote_no': u'0113101501682546', u'city_name': u'TANGERANG', u'manifest_date': u'15-MAR-2015 22:43', u'manifest_code': u'3', u'keterangan': u'Received On Destination'}]}
>>>
>>> # Show result with pretty print
>>> jne.tracking(airbill='0113101501682546', pretty_print=True)
{
  "cnote": {
    "city_name": "KOSAMBI / SELEMBARAN JATI",
    "cnote_date": "2015-03-14",
    "cnote_no": "1234567890123456",
    "cnote_pod_date": "18 Mar 2015  13:00",
    "cnote_pod_receiver": "UDIN",
    "cnote_receiver_name": "UDIN",
    "cnote_services_code": "REG",
    "pod_status": "DELIVERED"
  },
  "detail": [
    {
      "cnote_date": "14-03-2015 01:29",
      "cnote_destination": "KOSAMBI / SELEMBARAN JATI",
      "cnote_no": "1234567890123456",
      "cnote_origin": "JAKARTA",
      "cnote_receiver_addr1": "JL. SAHABAT NO. 11",
      "cnote_receiver_addr2": "RT 003/004",
      "cnote_receiver_addr3": "",
      "cnote_receiver_city": "KOSAMBI / SELEMBARAN",
      "cnote_receiver_name": "UDIN",
      "cnote_shipper_addr1": "PUNINAR LOGISTIC JL INSPEKSI",
      "cnote_shipper_addr2": "KIRANA NAGRAK CAKUNG DRAIN",
      "cnote_shipper_addr3": null,
      "cnote_shipper_city": "JAKARTA UTARA",
      "cnote_shipper_name": "SUDRAJAT",
      "cnote_weight": "1"
    }
  ],
  "ip": "192.168.2.228",
  "manifest": [
    {
      "city_name": "JAKARTA",
      "keterangan": "Manifested",
      "manifest_code": "1",
      "manifest_date": "14-MAR-2015 03:24",
      "mfcnote_no": "1234567890123456"
    },
    {
      "city_name": "TANGERANG",
      "keterangan": "Received On Destination",
      "manifest_code": "3",
      "manifest_date": "15-MAR-2015 22:43",
      "mfcnote_no": "1234567890123456"
    }
  ],
  "runsheet": [
    {
      "city_name": "TANGERANG",
      "drsheet_cnote_no": "1234567890123456",
      "mrsheet_date": "18-mar-2015 09:55",
      "pod_status": "ON PROCESS"
    }
  ]
}
>>>
```

#### 5. Find Nearby
---
```python
>>> jne.find_nearby(latitude='-6.1886183', longitude='106.8387325')
{u'places': [{u'custaddr1': u'JL CIKINI RAYA NO40 MENTENG JAKARTA PUSAT', u'custaddr2': None, u'jarak': u'     0.10', u'longitude': u'106.8385', u'custname': u'JNE ASP SEVEL CIKINI', u'latitude': u'-6.19164'}, {u'custaddr1': u'JL KWITANG RAYA NO 19-20 JAKARTA PUSAT', u'custaddr2': None, u'jarak': u'     0.26', u'longitude': u'106.8392', u'custname': u'JNE AGEN 0200033', u'latitude': u'-6.1808'}, {u'custaddr1': u'JL PEMBANGUNAN II NO 4 JAKARTA PUSAT', u'custaddr2': None, u'jarak': u'     0.27', u'longitude': u'106.83951', u'custname': u'JNE AGEN 0200006', u'latitude': u'-6.18073'}, {u'custaddr1': u'GD ALFA GLORIA PERKASA JL PEGANGSAAN TIMUR NO 1 CIKINI JAKARTA', u'custaddr2': None, u'jarak': u'     0.34', u'longitude': u'106.84045', u'custname': u'JNE AGEN 0200044', u'latitude': u'-6.19746'}, {u'custaddr1': u'MALL PLAZA ATRIUM LT 5 NO 8B SENEN JAKARTA PUSAT', u'custaddr2': None, u'jarak': u'     0.48', u'longitude': u'106.84177', u'custname': u'JNE AGEN 0200056', u'latitude': u'-6.17801'}]}
>>>
>>> # Show result with pretty print
>>> jne.find_nearby(latitude='-6.1886183', longitude='106.8387325', pretty_print=True)
{
  "places": [
    {
      "custaddr1": "JL CIKINI RAYA NO40 MENTENG JAKARTA PUSAT",
      "custaddr2": null,
      "custname": "JNE ASP SEVEL CIKINI",
      "jarak": "     0.10",
      "latitude": "-6.19164",
      "longitude": "106.8385"
    },
    {
      "custaddr1": "JL KWITANG RAYA NO 19-20 JAKARTA PUSAT",
      "custaddr2": null,
      "custname": "JNE AGEN 0200033",
      "jarak": "     0.26",
      "latitude": "-6.1808",
      "longitude": "106.8392"
    },
    {
      "custaddr1": "JL PEMBANGUNAN II NO 4 JAKARTA PUSAT",
      "custaddr2": null,
      "custname": "JNE AGEN 0200006",
      "jarak": "     0.27",
      "latitude": "-6.18073",
      "longitude": "106.83951"
    },
    {
      "custaddr1": "GD ALFA GLORIA PERKASA JL PEGANGSAAN TIMUR NO 1 CIKINI JAKARTA",
      "custaddr2": null,
      "custname": "JNE AGEN 0200044",
      "jarak": "     0.34",
      "latitude": "-6.19746",
      "longitude": "106.84045"
    },
    {
      "custaddr1": "MALL PLAZA ATRIUM LT 5 NO 8B SENEN JAKARTA PUSAT",
      "custaddr2": null,
      "custname": "JNE AGEN 0200056",
      "jarak": "     0.48",
      "latitude": "-6.17801",
      "longitude": "106.84177"
    }
  ]
}
>>>
```


#### Run Test
---
```
python -m unittest discover
```


Credits
-------
Thanks to [Widnyana](https://github.com/widnyana), this [script](https://github.com/widnyana/jne) is very useful :)

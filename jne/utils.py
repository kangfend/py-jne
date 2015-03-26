import json


def pretty_print(text):
    """This utils used for print pretty json"""
    print json.dumps(text, indent=2, sort_keys=True)

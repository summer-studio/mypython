#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import sys

def get_server_port(url):
    response = requests.get(url)
    print('response', response)
    response_json = json.loads(response.text)
    print('json', response_json)
    port = response_json['hosts'][0]['port']
    print(port)
    return port

if __name__ == '__main__':
    try:
        url = sys.argv[1]
        get_server_port(url)
    except Exception as e:
        print('args', sys.argv)
        print(e)
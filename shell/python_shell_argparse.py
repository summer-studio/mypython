#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import argparse


def get_server_port(url):
    response = requests.get(url)
    print('response', response)
    response_json = json.loads(response.text)
    print('json', response_json)
    port = response_json['hosts'][0]['port']
    print(port)
    return port

parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--url', '-u', help='url 属性，必要参数', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        get_server_port(args.url)
    except Exception as e:
        print('args:', args)
        print(e)

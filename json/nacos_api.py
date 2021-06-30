#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json


def get_server_port(url):
    response = requests.get(url)
    response_json = json.loads(response.text)
    port = response_json['hosts'][0]['port']
    return port


port = get_server_port(
    "http://10.4.23.53:8848/nacos/v1/ns/instance/list?serviceName=kk-member-server&groupName=DEFAULT_GROUP&namespaceId=b8293f1a-da23-4561-b6ae-920d5d662e5f")
print(port)

# if __name__ == '__main__':
#     try:
#         url = sys.argv[1:2]
#         get_server_port(url)
#     except Exception as e:
#         print(sys.argv)
#         print(e)

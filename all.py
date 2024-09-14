#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import data as d

def connect(end_point, post):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}
    response = requests.post(end_point, data=post, headers=headers)
    if response.status_code == 200:
        return response.json()
    return False

def produk():
    api_url = d.api_url
    post_data = {
        'api_key': d.api_key,
        'secret_key': d.secret_key,
        'action': 'services'
    }
    api_response = connect(api_url, post_data)
    print(api_response)

def order():
    api_url = data.api_url
    post_data = {
        'api_key': 'randomkey',
        'action': 'order',
        'secret_key': 'secret_key',
        'service': 1,
        'data': 'nasa',
        'quantity': 150
    }
    api_response = connect(api_url, post_data)
    print(api_response)

def cekorder():
    api_url = d.api_url
    post_data = {
        'api_key': d.api_key,
        'secret_key': d.secret_key,
        'action': 'status',
        'id': '9'
    }
    
    api_response = connect(api_url, post_data)
    print(api_response)

def profile():
    api_url = d.api_url
    post_data = {
        'api_key': d.api_key,
        'secret_key': d.secret_key,
        'action': 'profile'
    }
    
    api_response = connect(api_url, post_data)
    print(api_response)

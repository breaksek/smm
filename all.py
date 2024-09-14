#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import src.config as d

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
    target = input(" [•] Masukkan alamat target : ")
    jumlah = int(input("[•] Masukkan jumlah pesanan : "))
    api_url = d.api_url
    post_data = {
        'api_key': d.api_key,
        'secret_key': d.secret_key,
        'action': 'order',
        'service': idservice,
        'data': target,
        'quantity': jumlah
    }
    send = connect(api_url, post_data)
    print(send)

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

if __name__ == "__main__" :
    list()

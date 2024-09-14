#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import src.config as d
import os

def connect(end_point, post):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}
    response = requests.post(end_point, data=post, headers=headers)
    return response.json() if response.status_code == 200 else False

def produk():
    post_data = {
        'api_key': d.api_key,
        'secret_key': d.secret_key,
        'action': 'services'
    }
    print(connect(d.api_url, post_data))

def order():
    target = input(" [•] Masukkan alamat target : ")
    jumlah = int(input("[•] Masukkan jumlah pesanan : "))
    post_data = {
        'api_key': d.api_key,
        'secret_key': d.secret_key,
        'action': 'order',
        'service': idservice,  # Pastikan 'idservice' diinisialisasi sebelumnya
        'data': target,
        'quantity': jumlah
    }
    print(connect(d.api_url, post_data))

def cekorder():
    post_data = {
        'api_key': d.api_key,
        'secret_key': d.secret_key,
        'action': 'status',
        'id': '9'
    }
    print(connect(d.api_url, post_data))

def profile():
    post_data = {
        'api_key': d.api_key,
        'secret_key': d.secret_key,
        'action': 'profile'
    }
    api_response = connect(d.api_url, post_data)
    if api_response and 'data' in api_response:
        print(f"Username: {api_response['data'].get('username', 'Username tidak ditemukan')}")
    else:
        print("Gagal mendapatkan profil atau data tidak ada")

if __name__ == "__main__":
    # Pastikan ada menu() atau gunakan langsung fungsi
    profile()  # Contoh memanggil profile untuk dijalankan

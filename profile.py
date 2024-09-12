#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import requests
    import os
except Exception as k:
    exit(f"\n [•] Modul {k} tidak ditemukan")

try:
    import data as data
except Exception as ko:
    exit(f" [•] File {ko}.py Tidak ada")
    
def connect(end_point, post):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}
    response = requests.post(end_point, data=post, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
    return False

def get_profile():
    api_url = data.api_url
    post_data = {
        'api_key': data.api_key,
        'secret_key': data.secret_key,
        'action': 'profile'
    }
    api_response = connect(api_url, post_data)
    print(api_response)

if __name__ == "__main__":
    get_profile()

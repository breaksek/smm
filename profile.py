#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse

try:
    import requests
    import os
except Exception as k:
    print(f"\n [•] Kesalahan Modul :{k}")
    crot = urllib.parse.quote_plus(f"Error type : {k}")
    os.system(f"xdg-open https://wa.me/6281331184338?text={crot}")
    exit()

try:
    import data as data
except Exception as k:
    print(f" [•] Kesalahan File {k}")
    crot = urllib.parse.quote_plus(f"Error type : {k}")
    os.system(f"xdg-open https://wa.me/6281331184338?text={crot}")
    exit()
    
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
    os.system("git pull")
    get_profile()

import requests
import data as cok

def connect(end_point, post):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}
    response = requests.post(end_point, data=post, headers=headers)
    if response.status_code == 200:
        return response.json()
    return False

# Contoh membuat pesanan
api_url = cok.url
post_data = {
    'api_key': cok.api_key,
    'action': 'order',
    'secret_key': cok.secret_key,
    'service': 1,
    'data': 'nasa',
    'quantity': 150
}
api_response = connect(api_url, post_data)
print(api_response)

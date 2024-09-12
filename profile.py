import requests

def connect(end_point, post):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}
    response = requests.post(end_point, data=post, headers=headers)
    if response.status_code == 200:
        return response.json()
    return False

api_url = 'api_url'
post_data = {
    'api_key': 'randomkey',
    'secret_key': 'secret_key',
    'action': 'profile'
}
api_response = connect(api_url, post_data)
print(api_response)

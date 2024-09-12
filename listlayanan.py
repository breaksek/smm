import requests

def connect(end_point, post):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'}
    response = requests.post(end_point, data=post, headers=headers)
    if response.status_code == 200:
        return response.json()
    return False

# Contoh menampilkan layanan
api_url = 'https://buzzerpanel.id/api/json.php'
post_data = {
    'api_key': 'randomkey',
    'secret_key': 'secret_key',
    'action': 'services'
}
api_response = connect(api_url, post_data)
print(api_response)

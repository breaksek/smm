import requests
import data as data

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

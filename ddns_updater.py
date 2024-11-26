import requests

def get_public_ip():
    response = requests.get("https://api.ipify.org?format=text")
    return response.text


print(get_public_ip())
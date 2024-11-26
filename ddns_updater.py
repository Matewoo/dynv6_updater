import requests


dynv6_username = "" # Example: "55cjZFwRJ7URYRchE8WY5UHdVRnB5l"
dynv6_domain = "" # Example: "dynv6.net"

def get_public_ip():
    response = requests.get("https://api.ipify.org?format=text")
    return response.text

def call_api():
    
    try:
        response = requests.get(f"https://dynv6.com/api/update?hostname={dynv6_domain}&token={dynv6_username}&ipv4=" + get_public_ip())
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Fehler beim API-Aufruf: {e}")
        return None

api_response = call_api()

print(get_public_ip())
print(api_response)
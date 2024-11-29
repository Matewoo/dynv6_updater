import requests

def get_public_ip():
    response = requests.get("https://api.ipify.org?format=text")
    return response.text


def get_api_key():
    try:
        with open("api_key.txt") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("API-Schlüssel-Datei nicht gefunden.")
        return None

def get_domains():
    try:
        with open("domains.txt") as f:
            for line in f:
                D.append(line.strip())
        return D
    except FileNotFoundError:
        print("Domain-Datei nicht gefunden.")
        return None

def call_api(d):
    try:
        response = requests.get(f"https://dynv6.com/api/update?hostname={d}&token=" + str(get_api_key()) + "&ipv4=" + (get_public_ip()))
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        response = (f"error with API call: {e}")
        return response

D = []
get_domains()
print("domains are getting updated with ip: " + get_public_ip())
print("")

for d in D:
    api_response = call_api(d)
    print(f"{d}: {api_response}")

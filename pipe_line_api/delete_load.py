import requests

def obtain_load_name() -> str:
    url = "http://localhost:8002/api/loads/current"
    resp = requests.get(url)
    data = resp.json()
    return data["data"]["name"]


requests.delete("http://localhost:8002/api/loads/"+obtain_load_name())
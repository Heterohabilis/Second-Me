import requests

url = "http://localhost:8002/api/loads"
payload = {
    "name": "cybercricetus",
    "description": "This is a cybercricetus, a CS student,"
                   "game lover, and a cricetus.",
    "email": "test@example.com"
}
resp = requests.post(url, json=payload)
print(resp.status_code)
print(resp.json())
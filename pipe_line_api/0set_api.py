import os

import requests

URL = "http://localhost:8002/api/user-llm-configs"
BASE = "https://ark.cn-beijing.volces.com/api/v3"
CHAT_NAME = 'ep-20250122121527-wwskz'
EMB_NAME = 'ep-20250126101111-bqjdm'
PROVIDER_TYPE = 'litellm'
API_KEY = os.environ['MODEL_KEY']
print(API_KEY)

payload = {
    "chat_api_key" : API_KEY,
    "chat_endpoint": BASE,
    "chat_model_name": CHAT_NAME,
    "embedding_api_key": API_KEY,
    "embedding_endpoint": BASE,
    "embedding_model_name": EMB_NAME,
    "provider_type": PROVIDER_TYPE,
}

headers = {
    "Content-Type": "application/json"
}

response = requests.put(URL, json=payload, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.json())
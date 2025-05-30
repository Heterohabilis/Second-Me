import requests

url = "http://localhost:8002/api/memories/file"

files = [
    ('file', open('/Users/bytedance/Downloads/2.pdf', 'rb')),
]

data = {
    'user_id': '123',
    'description': 'multiple files uploading'
}

response = requests.post(url, files=files, data=data)

print(response.status_code)
print(response.json())
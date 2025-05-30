import requests

try:
    with requests.get("http://localhost:8002/api/trainprocess/logs", stream=True) as r:
        for line in r.iter_lines():
            if line.decode().startswith(':'):
                continue
            if line:
                print(line.decode())
except KeyboardInterrupt:
    print('DONE')
import requests
import json

url = 'http://0.0.0.0:5000/api/'

data = 'How can you help?'
# j_data = json.dumps(data)
headers = {'content-type': 'text/plain', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=data, headers=headers)
print(r, r.text)
import requests
import json

url = 'http://127.0.0.1:5000/api/'

data = 'How can you help?'
# j_data = json.dumps(data)
headers = {'content-type': 'text/pain', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=data, headers=headers)
print(r, r.text)
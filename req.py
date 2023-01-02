import json

import requests

status = 'sold'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept':'application/json'})


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.post(f'https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(info, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

res = requests.delete(f'https://petstore.swagger.io/v2/pet/id', headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.put(f'https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(info, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))
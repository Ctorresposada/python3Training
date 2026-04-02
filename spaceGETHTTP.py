import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)
print("\n")
print("\n")


for astronaut in json['people']:
    print(astronaut['name'])
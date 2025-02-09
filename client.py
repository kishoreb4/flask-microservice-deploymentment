import requests
response = requests.get('http://192.168.1.7:5000/api')
print(response.json())
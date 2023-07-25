import requests

endpoint = 'http://localhost:8000/api/products/13665652433434223/'

get_response = requests.get(endpoint)
print(get_response.json())
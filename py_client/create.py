import requests

headers = {
    'Authorization': 'Bearer e1e8eed0b0b30c4ae3f5bfa3acad86e2e96e45e8 '
    }
endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': 'This field is done',
    'price': 12.00
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
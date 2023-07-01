import requests

headers = {
    'Authorization': 'Bearer b3fe3bab59a270c9595c6e021c1706efeac03e56 '
    }
endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': 'This field is done',
    'price': 12.00
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
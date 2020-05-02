import requests
URL = 'http://localhost:8000/api/v1/cards/transactions'
URL2 = 'http://localhost:8005/'
resp = requests.post(URL, data={'content': 'hello'}, auth=('hung', 'poscard123'))
resp = requests.post(URL2, data={'content': 'hello'}, auth=('hung', 'poscard123'))


import requests
import jwt
import sys
# URL = 'http://localhost:8000/api/v1/cards/detect'
URL = 'http://poscard.local:8000/api/v1/cards/add'
secretkey = 'kJDFP(*&(*!UER5123UFD*(74ioPJSDfkjijraefASD^%#$*'
while True:
    card = input()
    data={'card_id': card}
    encoded = jwt.encode(data, secretkey, algorithm='HS256')
    try:
        resp = requests.post(URL, data={'content': encoded})
        print(resp.status_code)
    except Exception as e:
        print('Connection error')
        print(e)


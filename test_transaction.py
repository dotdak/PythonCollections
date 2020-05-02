import requests
import jwt
import sys
URL = 'http://localhost:8000/api/v1/cards/transactions'
secretkey = 'kJDFP(*&(*!UER5123UFD*(74ioPJSDfkjijraefASD^%#$*'
data={'card_id': '0628833060', 'payment': int(sys.argv[1])}
encoded = jwt.encode(data, secretkey, algorithm='HS256')
resp = requests.post(URL, data={'content': encoded})


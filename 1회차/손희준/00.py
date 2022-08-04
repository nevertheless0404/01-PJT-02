from unittest.case import _BaseTestCaseContext
import requests


order_currency = 'BTC'
payment_currency = 'KRW'
prev_closing_price = 'KRW'

URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(URL)

data = response.json()
print(data.get('data').get('prev_closing_price'))



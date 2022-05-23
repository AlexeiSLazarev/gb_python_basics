from locale import currency
from requests import get, utils
import xmltodict
from datetime import datetime
from dateutil import parser

def currency_rates(currency_):
    currency_value = 0
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    dict_data = xmltodict.parse(response.content)
    request_date = parser.parse(dict_data['ValCurs']['@Date']).date()
    for i in range(len(dict_data['ValCurs']['Valute'])):
        if dict_data['ValCurs']['Valute'][i]['CharCode'] == currency_:
            currency_value = dict_data['ValCurs']['Valute'][i]['Value']
    
    return [request_date, currency_value]


# request_date, currency_value = currency_rates('EUR')
# print(request_date)
# print(currency_value)
#!/usr/bin/env python
import requests
import json
import argparse
import sys

# Create command line arguments
parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-a','--amount', help='The amount to be converted', required=True)
parser.add_argument('-i','--input_currency', help='Input currency', required=True)
parser.add_argument('-o','--output_currency', help='Output currency', required=False)

results = parser.parse_args()

# Dictionary to store the currency symbols along with the currency names
SYMBOLS_CURRENCIES = {
    '€': 'EUR',
    'A$': 'AUD',
    'R$': 'BRL',
    'C$': 'CAD',
    'C¥': 'CNY',
    'Kč': 'CZK',
    'dkr': 'DKK',
    '£': 'GBP',
    'HK$': 'HKD',
    'kn': 'HRK',
    'Ft': 'HUF',
    'Rp': 'IDR',
    '₪': 'ILS',
    '₹': 'INR',
    'J¥': 'JPY',
    '₩': 'KRW',
    'Mex$': 'MXN',
    'RM': 'MYR',
    'NZ$': 'NZD',
    '₱': 'PHP',
    'zł': 'PLN',
    'lei': 'RON',
    '₽': 'RUB',
    'skr': 'SEK',
    'S$': 'SGD',
    '฿': 'THB',
    '₺': 'TRY',
    '$': 'USD',
    'R': 'ZAR',
};


def get_current_rate(base, target=None):
    """
    This function makes a call to the FIXER api and returns the exchange rates in JSON format
    """
    if target:
        if base in SYMBOLS_CURRENCIES:
            base = SYMBOLS_CURRENCIES[base]
        if target in SYMBOLS_CURRENCIES:
            target = SYMBOLS_CURRENCIES[target]
        r = requests.get('http://api.fixer.io/latest?base={0}&symbols={1}'.format(base, target))
    else:
        if base in SYMBOLS_CURRENCIES:
            base = SYMBOLS_CURRENCIES[base]
        r = requests.get('http://api.fixer.io/latest?base={0}'.format(base))
    return r.json()

def convert_currency(base, amount, target=None):
    if target:
        json_response = get_current_rate(base, target)
        if target in SYMBOLS_CURRENCIES:
            target = SYMBOLS_CURRENCIES[target]
        try:
            rate = json_response['rates'][target]
        except KeyError:
            print('The currency should be a valid currency e.g. EUR, GBP etc')
            sys.exit(1)
        try:
            result = float(amount) * rate
        except ValueError:
            print('The amount should be a float or integer number.')
            sys.exit(1)
    else:
        json_response = get_current_rate(base)
        currencies = []
        try:
            for cur in json_response['rates']:
                currencies.append(cur)
        except KeyError:
            print('The currency should be a valid currency e.g. EUR, GBP etc')
            sys.exit(1)
        result = {}
        for cur in currencies:
            try:
                result[cur] = float(amount) * json_response['rates'][cur]
            except ValueError:
                print('The amount should be a float or integer number.')
                sys.exit(1)
    return result

def create_json_response(base, amount, result, target=None):
    """
    This function creates the json with the required structure
    """
    data = {}
    data['input'] = {}
    data['input']['amount'] = amount
    if base in SYMBOLS_CURRENCIES:
        base = SYMBOLS_CURRENCIES[base]
    data['input']['currency'] = base
    data['output'] = {}
    if target:
        if target in SYMBOLS_CURRENCIES:
            target = SYMBOLS_CURRENCIES[target]
        data['output'][target] = result
    else:
        for key, value in result.items():
            data['output'][key] = value
    json_result = json.dumps(data)
    return json.loads(json_result)

result = convert_currency(results.input_currency, results.amount, results.output_currency)

json_data = create_json_response(results.input_currency, results.amount, result, results.output_currency)

print(json.dumps(json_data, indent=4, sort_keys=True))

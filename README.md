# Currency converter in Python
This currency converter is built in Python using exchange rates from [Fixer.io API](http://fixer.io/)

## Prerequisities
* Python 3
* pip

## Run instructions
1. Clone the repository
2. pip install -r requirements.txt
3. python currency_converter.py --amount (VALUE) --input_currency (VALUE) --output_currency (VALUE)

The amount is the amount which we want to convert (float)

The input and the output currencies are the currencies currently supported by the [Fixer.io API](http://fixer.io/).
(AUD,BGN,BRL,CAD,CHF,CNY,CZK,DKK,GBP,HKD,HRK,HUF,IDR,ILS,INR,JPY,KRW,MXN,MYR,NOK,NZD,PHP,PLN,RON,RUB,SEK,SGD,THB,TRY,USD,ZAR)

The output currency is optional. In case of not providing a value, the script converts to all known currencies.

Moreover, you can use the following symbols as input or output currencies
```
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
```

## Examples
```
./currency_converter.py --amount 53.93 --input_currency EUR --output_currency USD
{
    "input": {
        "amount": "53.93",
        "currency": "EUR"
    },
    "output": {
        "USD": 57.106477
    }
}
```
```
./currency_converter.py --amount 53.93 --input_currency € --output_currency $
{
    "input": {
        "amount": "53.93",
        "currency": "EUR"
    },
    "output": {
        "USD": 57.106477
    }
}
```
```
./currency_converter.py --amount 53.93 --input_currency ₱
{
    "input": {
        "amount": "53.93",
        "currency": "PHP"
    },
    "output": {
        "AUD": 1.48949267,
        "BGN": 2.01843811,
        "BRL": 3.4990323299999995,
        "CAD": 1.44882945,
        "CHF": 1.10685932,
        "CNY": 7.5599074,
        "CZK": 27.8861244,
        "DKK": 7.6720818,
        "EUR": 1.0320044800000001,
        "GBP": 0.8839126999999999,
        "HKD": 8.4750995,
        "HRK": 7.8203892999999995,
        "HUF": 317.07604200000003,
        "IDR": 14605.3226,
        "ILS": 4.191817110000001,
        "INR": 74.29936099999999,
        "JPY": 126.76246499999999,
        "KRW": 1301.76234,
        "MXN": 23.2503016,
        "MYR": 4.88751411,
        "NOK": 9.2743421,
        "NZD": 1.5555569200000001,
        "PLN": 4.49463406,
        "RON": 4.6454223400000005,
        "RUB": 64.759144,
        "SEK": 9.8573254,
        "SGD": 1.5654800400000002,
        "THB": 38.9687394,
        "TRY": 3.95312293,
        "USD": 1.09278359,
        "ZAR": 14.8798263
    }
}
```

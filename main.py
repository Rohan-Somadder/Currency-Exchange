import requests
from API import API_KEY
from API import CURR

LINK = "https://v6.exchangerate-api.com/v6/"


class CurrencyExchange():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.rates = self.data['conversion_rates']
        self.currencies = self.data['conversion_rates'].keys()

    def convert(self, to_currency, amount):
        # limiting the precision to 4 decimal places
        amount = round(amount * self.rates[to_currency], 4)
        return amount


def exchange():
    ''' Function for exchange of the currencies'''
    currency_code = input("Enter the currency code: ")
    if currency_code not in CURR:
        print(f"{currency_code} is not supported, changing the base currency to USD...")
        currency_code = "USD"

    url = LINK + API_KEY + "/latest/" + currency_code

    currency = CurrencyExchange(url)

    exchange_code = input("Enter the exchange currency code: ")
    if exchange_code not in CURR:
        print(
            f"{exchange_code} is currently not supported for exchange, converting to EUR...")
        exchange_code = "EUR"

    amount = input("Enter the amount of currency to convert: ")
    try:
        amount = float(amount)
    except ValueError:
        print("The input amount you entered is incorrect, input amount set to 1...")
        amount = 1

    print(f"{amount} {currency_code} = {currency.convert(exchange_code,amount)} {exchange_code}")


def main():
    ''' Handles the greetings and initial displays'''
    print('CURRENCY EXCHANGE APP'.center(51, '='), "\n")
    exchange()


if __name__ == '__main__':
    main()

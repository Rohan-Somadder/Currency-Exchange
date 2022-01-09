from API import API_KEY
from API import CURR
import requests

LINK = "https://v6.exchangerate-api.com/v6/"


class CurrencyExchange():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['conversion_rates'].keys()

    def convert(self, to_currency, amount):
        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


def main():
    currency_code = input("Enter the currency code: ")
    if currency_code not in CURR:
        currency_code = "USD"

    url = LINK + API_KEY + "/latest/" + currency_code
    currency = CurrencyExchange(url)

if __name__ == '__main__':
    main()

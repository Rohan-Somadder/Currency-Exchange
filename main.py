'''
Basic Currency Exchange Application based on ExchangeRate-Api

# Todo: None
'''

import requests
from api import API_KEY
from api import CURR


LINK = "https://v6.exchangerate-api.com/v6/"


class CurrencyExchange():
    ''' Class for the currency.'''

    def __init__(self, url):
        #self.data = requests.get(url).json()
        self.rates = requests.get(url).json()['conversion_rates']

    def convert(self, to_currency, amount):
        '''Converts given amount to value in given currency'''
        # limiting the precision to 4 decimal places
        amount = round(amount * self.rates[to_currency], 4)
        return amount

    def compare(self, first_currency, second_currency):
        '''Compares the two different currencies'''
        if self.rates[first_currency] < self.rates[second_currency]:
            eq_amt = self.rates[second_currency]/self.rates[first_currency]
            print(f"\n{first_currency} is more valuable than {second_currency}")
            print(f"1 {first_currency} = {eq_amt} {second_currency}\n")

        elif self.rates[first_currency] > self.rates[second_currency]:
            eq_amt = self.rates[first_currency]/self.rates[second_currency]
            print(f"\n{second_currency} is more valuable than {first_currency}")
            print(
                f"1 {second_currency} = {eq_amt} {first_currency}\n")

        else:
            print("\nBoth are of same value.\n")


def exchange():
    ''' Function for exchange of the currencies'''
    currency_code = input("\nEnter the currency code: ").upper()
    if currency_code not in CURR:
        print(
            f"\n{currency_code} is not supported, changing the base currency to USD...")
        currency_code = "USD"

    url = LINK + API_KEY + "/latest/" + currency_code

    currency = CurrencyExchange(url)

    exchange_code = input("\nEnter the exchange currency code: ").upper()
    if exchange_code not in CURR:
        print(
            f"\n{exchange_code} is currently not supported for exchange, converting to EUR...")
        exchange_code = "EUR"

    amount = input("\nEnter the amount of currency to convert: ")
    try:
        amount = float(amount)
    except ValueError:
        print("\nThe input amount you entered is incorrect, input amount set to 1...")
        amount = 1

    print(f"{amount} {currency_code} = {currency.convert(exchange_code,amount)} {exchange_code}\n")


def compare():
    ''' Function to compare currencies based on USD'''
    url = LINK + API_KEY + "/latest/USD"

    currency = CurrencyExchange(url)

    curr_1 = input("\nEnter currency code for first currency: ").upper()
    if curr_1 not in CURR:
        print(
            f"\n{curr_1} is currently not supported for exchange, converting to EUR...")
        curr_1 = "EUR"

    curr_2 = input("\nEnter currency code for second currency: ").upper()
    if curr_2 not in CURR:
        print(
            f"\n{curr_2} is currently not supported for exchange, converting to INR...")
        curr_2 = "INR"

    currency.compare(curr_1, curr_2)


def main():
    ''' Handles the greetings and initial displays'''
    choice = 1
    while choice in [1, 2]:
        print('CURRENCY EXCHANGE APP'.center(51, '='), "\n\n")
        print('MENU'.center(51, '-'), '\n')
        print('1.     Exchange currency')
        print('2.     Comapre Currencies')
        print('Else.  Exit')
        try:
            choice = int(input('Enter :  '))
        except ValueError:
            choice = -1
        if choice == 1:
            exchange()
        if choice == 2:
            compare()


if __name__ == '__main__':
    main()

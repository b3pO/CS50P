import requests
import json
import sys


"""Format the price to d number of decimal places"""
def format_price(price, d):
    pre_formatted = float(price)
    formatted = "{:.{}f}".format(pre_formatted, d)
    return float(formatted)

"""Get the stats for that particular coin"""
def get_coin_stats(coin, contents):
    for c in contents["data"]:
        if c["id"] == coin:
            return c

"""Retrieves data for top 100 coins from the CoinCap API"""
def get_data():
    try:
        data = requests.get("https://api.coincap.io/v2/assets/")
        data.raise_for_status()
    except requests.HTTPError:
        print("Could not connect to CoinCap API.")
        sys.exit(1)

    data = data.json()
    return data

"""Prompts user for amount of coins until a valid response is given"""
def how_many_coins():
    while True:
        response = input("How many coins would you like? ")
        try:
            amount = float(response)
        except ValueError:
            print("Please enter a number.")
            continue
        return amount

"""Returns true when the coin entered is valid"""
def is_coin(coin, coins):
    if coin in coins:
        return True
    else:
        return False

"""Prompts the user for the coin they would like to look up"""
def which_coin(coins):
    while True:
        response = input("Which coin would you like to inquire about? ")
        if response not in coins:
            print("That coin is not in the top 100 at the moment.")
            continue
        else:
            return response

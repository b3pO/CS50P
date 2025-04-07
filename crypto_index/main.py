from crypto import *


def main():
    contents = get_data()
    coins = [coin["id"] for coin in contents["data"]]

    if len(sys.argv) > 1:
        if len(sys.argv) > 3:
            print("Usage: python crypto.py <coin-name> <amount>")
            sys.exit(1)
        elif is_coin(sys.argv[1], coins) == 0:
            print("That coin is not in the top 100 at the moment.")
            sys.exit(1)

        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Usage: python crypto.py <coin-name> <amount>")
            sys.exit(1)
        except IndexError:
            amount = how_many_coins()

        stats = get_coin_stats(sys.argv[1], contents)
        price = format_price(stats["priceUsd"], 4)
        total = amount * price

        print(f"${total:,} USD")

    else:
        print("Welcome to the CoinCap Price Index!")
        coin = which_coin(coins)
        amount = how_many_coins()
        stats = get_coin_stats(coin, contents)

        price = format_price(stats["priceUsd"], 4)
        total = amount * price
        
        print(f"${total:,} USD")


if __name__ == "__main__":
    main()
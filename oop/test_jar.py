from jar import Jar


def main():
    jar = Jar()
    withdraw_cookies(jar)

def deposit_cookies(jar):
    n = 1
    for x in range(jar.capacity + 1):
        jar.deposit(n)
        print(jar)

def withdraw_cookies(jar):
    jar.deposit(jar.capacity)
    n = 1
    for x in range (jar.capacity + 1):
        jar.withdraw(n)
        print(jar)


if __name__ == "__main__":
    main()
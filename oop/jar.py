class Jar:
    cookies = 0
    cookie_emoji = "\U0001f36a"

    def __init__(self, capacity=12):
        if not capacity >= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity

    def __str__(self):
        return self.cookie_emoji * self.cookies

    def deposit(self, n):
        if (self.cookies + n) > self.capacity:
            raise ValueError("Over the limit!")
        self.cookies = self.cookies + n

    def withdraw(self, n):
        if (self.cookies - n) < 0:
            raise ValueError("Not enough cookies!")
        self.cookies = self.cookies - n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies

    
def main():
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(5)
    print(jar)
    print(jar.size)
        

if __name__ == "__main__":
    main()
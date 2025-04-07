class SodaMachine:
    sodas = {
        "E1": ("Coke", 1.50), "E2": ("Sprite", 1.50), "E3": ("Diet Coke", 1.50), 
        "F1": ("Dr. Pepper", 1.50), "F2": ("Mellow Yellow", 1.50), 
        "F3": ("Dasani Water", 2.00), "G1": ("Vitamin Water", 2.50), "G2": ("Monster", 3.50)
        }
    accepted_coins = [.25, .10, .05]
    
    def select(self):
        self.selection = input("Enter selection: ").upper()
        self.soda_tuple = self.sodas[self.selection]
        self.cost = self.soda_tuple[1]

    def collect(self, cost):
        due = cost
        while due > 0:
            print("Amount Due: ", due)
            try:
                entry = float(input("Insert Coin: "))
                if entry not in self.accepted_coins:
                    continue
            except ValueError:
                continue
            due = round((due - entry), 2)
        print("Change Owed: ", (due * -1))


def main():
    machine = SodaMachine()
    machine.select()
    machine.collect(machine.cost)
    

if __name__ == "__main__":
    main()

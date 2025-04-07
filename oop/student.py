class Wizard:
    def __init__(self, name, patronus=None):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"Professor {self.name} teaches {self.subject}"

    @classmethod
    def get(cls):
         name = input("Name: ")
         subject = input("Subject: ")
         return cls(name, subject)

class Student(Wizard):
    def __init__(self, name, house, patronus):
        super().__init__(name, patronus)
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} | Patronus: {self.patronus}"
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
         name = input("Name: ")
         house = input("House: ")
         patronus = input("Patronus: ")
         return cls(name, house, patronus)


""""
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)"
"""
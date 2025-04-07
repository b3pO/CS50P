from hat import Hat
from student import Student, Professor, Wizard


def main():
    """Hat.sort("Harry")"""

    wizard = Wizard("Albus")
    student = Student.get()
    professor = Professor.get()
    print(student)
    print(professor)

if __name__ == "__main__":
    main()
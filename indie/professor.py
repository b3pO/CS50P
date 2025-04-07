import random


def main():
    level = get_level()
    sign = get_sign()
    score = generate_equation(level, sign)
    print(f"Score: {score}")

"""Prompts the user for a level, n.
If the user does not input 1, 2, or 3, the program should prompt again"""
def get_level():
    while True:
        level = input("Enter a level from 1 to 3: ")
        try:
            level = int(level)
        except ValueError:
            continue
        if level > 0 and level < 4:
            return level
        
def get_sign():
    while True:
        response = input("Enter mode (+ - * /):  ")
        if response == '+' or response == '-' or response == '*' or response == '/':
            return response
        else:
            continue

"""Randomly generates ten (10) math problems formatted as X + Y = ,
wherein each of X and Y is a non-negative integer with n digits"""
def generate_equation(level, sign):
    score = 0

    if level == 2:
        start = 10
        end = 99
    elif level == 3:
        start = 100
        end = 999
    else:
        start = 1
        end = 10

    for i in range(10):
        if sign == '+':
            first = random.randint(start, end)
            second = random.randint(start, end)
            answer = first + second
        elif sign == '*':
            first = random.randint(start, end)
            second = random.randint(start, end)
            answer = first * second
        elif sign == '-':
            while True:
                first = random.randint(start, end)
                second = random.randint(start, end)
                if first > second:
                    answer = first - second
                    break
                else:
                    continue
        elif sign == '/':
            while True:
                first = random.randint(start, end)
                second = random.randint(start, end)
                if (first % second == 0) and (first / second != 1):
                    answer = first / second
                    break
                else:
                    continue

        response = equate(first, second, answer, sign)
        if response == answer:
            score += 1   
    return score

def equate(first, second, answer, sign):
    retries = 0
    while True:
        """Prints correct answer if an incorrect type is given 3 times"""
        while retries < 3:
            try:
                response = int(input(f"{first} {sign} {second} = "))
                return response
            except ValueError:
                print("EEE ")
                retries += 1
        break
    print(answer)


if __name__ == "__main__":
    main()
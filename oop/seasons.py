from datetime import date


class Birthday:
    months = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
        6: "June", 7: "July", 8: "August", 9: "September",
        10: "October", 11: "November", 12: "December"      
        }

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.written_month = self.months[month]
        
    def __str__(self):
        return f"{self.written_month} {self.day}, {self.year}"


def main():
    birthday = get_birthday()
    today = date.today()
    
    user_birthday = date(birthday.year, birthday.month, birthday.day)
    days_since_birth = today - user_birthday
    minutes_since_birth = days_since_birth.days * 1440

    print(f"{birthday} was {minutes_since_birth} minutes ago! Feeling old yet?")

def get_birthday():
    while True:
        try:
            dob = input("Enter your date of birth (YYYY-MM-DD): ")
            year, month, day = dob.split('-')
            year = int(year)
            month = int(month)
            day = int(day)
            if year < 1900 or year > 2020 or month < 1 or month > 12 or day < 1 or day > 31:
                continue
        except ValueError:
            continue

        birthday = Birthday(year, month, day)
        return birthday



if __name__ == "__main__":
    main()




from datetime import datetime

class Person:
    def __init__(self):
        name = input("Enter your name: ")
        country = input("Enter your country: ")
        day = int(input("Enter your birth date (DD): "))
        month = int(input("Enter your birth month (MM): "))
        year = int(input("Enter your birth year (YYYY): "))

        self.__name = name
        self.__country = country
        self.__day = day
        self.__month = month
        self.__year = year

    def age(self):
        today = datetime.now()
        dob_date = datetime(self.__year, self.__month, self.__day)
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        print("Name:", self.__name)
        print("Country:", self.__country)
        print("Age:", age)

def main():
    person = Person()
    person.age()

if __name__ == "__main__":
    main()

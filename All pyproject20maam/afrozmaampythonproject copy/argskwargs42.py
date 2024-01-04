#Write a program to take input as name, email & age from user using
#combination of keywords argument and positional arguments (*args
#and**kwargs) using function,
def get_user_details(*args, **kwargs):
    if 'name' in kwargs and 'email' in kwargs and 'age' in kwargs:
        name = kwargs['name']
        email = kwargs['email']
        age = kwargs['age']
    elif len(args) == 3:
        name, email, age = args
    else:
        print("Invalid input. Provide either name, email, and age as keyword arguments or as positional arguments.")
        return

    print("User Details:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Age: {age}")
name_input = input("Enter your name: ")
email_input = input("Enter your email: ")
age_input = input("Enter your age: ")

get_user_details(name=name_input, email=email_input, age=int(age_input))


import random

loop_program =  True

print("Welcome to Random Bank!")
name = input("What is your name? ")
print(f"Nice to meet you {name}! May I ask your age? ")
age = int(input("What is your age? "))
print(f"{age}, what a wonderful age to be!")
location = input("Where do you live, for our records? ")
print(f"{location}? I love that place!")
contact = input("Finally, so we can reach you, could I have a phone number or email? ")


def options():
    print("\n Please chose from the following options: ")
    print("1. Checking")
    print("2. Savings")
    print("3. Exit the conversation")

def user_selection():
    in_use = True
    user_choice = int(input("Enter a number 1-3: "))
    if user_choice == 1:
        print("This is the first placeholder.")
    elif user_choice == 2:
        print("This is the second placeholder.")
    elif user_choice == 3:
        print("Exiting the program, thank you for visiting!")
        in_use = False
    else:
        print("Sorry, that wasn't a valid option, please choose again.")
    return in_use

while loop_program:
    options()
    loop_program = user_selection()
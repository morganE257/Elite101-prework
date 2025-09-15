import random

loop_program =  True

print("Welcome to the Elite 101 chatbot!")
name = input("What is your name? ")
age = int(input(f"Hello {name}, how old are you? "))
if age <= 15:
    print(f"Oh, {age}, to be young again! What can I do for you? ")
else:
    print(f"{age}, a wonderful age to be! What can I do for you? ")


def options():
    print("\n Please chose from the following options: ")
    print("1. Placeholder Option 1")
    print("2. Placeholder Option 2")
    print("3. Placeholder Option 3")
    print("4. Exit the conversation")

def user_selection():
    in_use = True
    user_choice = int(input("Enter a number 1-4: "))
    if user_choice == 1:
        print("This is the first placeholder.")
    elif user_choice == 2:
        print("This is the second placeholder.")
    elif user_choice == 3:
        print("This is the third placeholder.")
    elif user_choice == 4:
        print("Exiting the program, thank you for visiting!")
        in_use = False
    else:
        print("Sorry, that wasn't a valid option, please choose again.")
    return in_use

while loop_program:
    options()
    loop_program = user_selection()
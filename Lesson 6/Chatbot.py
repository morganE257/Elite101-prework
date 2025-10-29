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
        print("Alright, you want to make a checking account.")
        print("First, I want you to confirm just in case.")
        confirm = input("Do you want to make a checking account? ")
        if confirm == "Yes" or confirm == "yes":
            print("Alright, lets continue!")
            account_number = random.randint(1,1000)
            print(f"Your account number is {account_number}.")
        else:
            print("Alright, please pick another option.")

        account_pin_number = int(input("Okay, what is your pin for this account?" ))
        print(f"Okay, your pin number is {account_pin_number}")
        cont = input("Would you like to continue with your account?" )
        if cont == "yes" or cont == "Yes":
            money = input("Would you like to make a withdrawl or a deposit? ")
            if money == "Withdrawl" or money == "withdrawl":
                withdrawl = int(input("Alright, how much would you like to take out? "))
                print(f"Okay, you have withdrawn ${withdrawl}")
            elif money == "deposit" or money == "Deposit":
                deposit = int(input("Okay, how much would you like to deposit?"))
                print(f"Okay, you have deposited ${deposit}.")
            else:
                print("Have a good day!")
        else:
            print("Have a good day!")

    elif user_choice == 2:
        print("Savings.")
        print("Alright, you want to make a savings account.")
        print("First, I want you to confirm just in case.")
        confirm = input("Do you want to make a savings account? ")
        if confirm == "Yes" or confirm == "yes":
            print("Alright, lets continue!")
            account_number = random.randint(1,1000)
            print(f"Your account number is {account_number}.")
        else:
            print("Alright, please pick another option.")
        account_pin_number = int(input("Okay, what is your pin for this account?" ))
        print(f"Okay, your pin number is {account_pin_number} ")
        cont = input("Would you like to continue with your account? ")
        if cont == "yes" or cont == "Yes":
            money = input("Would you like to make a withdrawl or a deposit? ")
            if money == "Withdrawl" or money == "withdrawl":
                withdrawl = int(input("Alright, how much would you like to take out? "))
                print(f"Okay, you have withdrawn ${withdrawl}")
            elif money == "deposit" or money == "Deposit":
                deposit = int(input("Okay, how much would you like to deposit?"))
                print(f"Okay, you have deposited ${deposit}.")
            else:
                print("Have a good day!")
        else:
            print("Have a good day!")
    elif user_choice == 3:
        print("Exiting the program, thank you for visiting!")
        in_use = False
    else:
        print("Sorry, that wasn't a valid option, please choose again.")
    return in_use

while loop_program:
    options()
    loop_program = user_selection()
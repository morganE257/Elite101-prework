import random

#Makes the program keep looping until false
loop_program =  True

#Intro/Information collection
print("Welcome to Random Bank!")
name = input("What is your name? ") #Collect user name
#Uses the users name input, print out greeting and user name.
print(f"Nice to meet you {name}! May I ask your age? ") 
age = int(input("What is your age? ")) #Collects user age in int
#Uses the users age input, print out user age and extra content.
print(f"{age}, what a wonderful age to be!")
location = input("Where do you live, for our records? ") #Collects user location
#Uses user location input, prints out location.
print(f"{location}? I love that place!")
contact = input("Finally, so we can reach you, could I have a phone number or email? ")

#Prints out options for user
def options():
    print("\n Please chose from the following options: ")
    print("1. Checking")
    print("2. Savings")
    print("3. Exit the conversation")

def user_selection():
    in_use = True
    #Lets the user choose an option
    user_choice = int(input("Enter a number 1-3: "))
    #user chooses option 1
    if user_choice == 1:
        print("Alright, you want to make a checking account.")
        print("First, I want you to confirm just in case.")
        confirm = input("Do you want to make a checking account? ")
        #Checks if user wants to continue with chosen account
        if confirm == "Yes" or confirm == "yes":
            print("Alright, lets continue!")
            account_number = random.randint(1,1000) #Assigns an account number for the user
            print(f"Your account number is {account_number}.")
            #Takes in the users chosen pin number
            account_pin_number = int(input("Okay, what is your pin for this account? "))
            print(f"Okay, your pin number is {account_pin_number}")
            #Checks if the user wants to continue with account
            cont = input("Would you like to continue with your account? ")
            if cont == "yes" or cont == "Yes":
                #Will the user withdrawal or deposit an amount
                money = input("Would you like to make a withdrawal or a deposit? ")
                if money == "Withdrawal" or money == "withdrawal":
                    #How much the user wants to withdrawal (Assume the money is in the account)
                    withdrawal = int(input("Alright, how much would you like to take out? "))
                    print(f"Okay, you have withdrawn ${withdrawal}")
                elif money == "deposit" or money == "Deposit":
                    #How much the user wants to deposit
                    deposit = int(input("Okay, how much would you like to deposit? "))
                    print(f"Okay, you have deposited ${deposit}.")
                else:
                    print("Have a good day!")
        else:
            print("Alright, please pick another option.")

    #user chooses option 2
    elif user_choice == 2:
        print("Savings.")
        print("Alright, you want to make a savings account.")
        print("First, I want you to confirm just in case.")
        confirm = input("Do you want to make a savings account? ")
        if confirm == "Yes" or confirm == "yes":
            print("Alright, lets continue!")
            account_number = random.randint(1,1000)
            print(f"Your account number is {account_number}.")
            account_pin_number = int(input("Okay, what is your pin for this account?" ))
            print(f"Okay, your pin number is {account_pin_number} ")
            cont = input("Would you like to continue with your account? ")
            if cont == "yes" or cont == "Yes":
                money = input("Would you like to make a withdrawal or a deposit? ")
                if money == "Withdrawal" or money == "withdrawal":
                    withdrawal = int(input("Alright, how much would you like to take out? "))
                    print(f"Okay, you have withdrawn ${withdrawal}")
                elif money == "deposit" or money == "Deposit":
                    deposit = int(input("Okay, how much would you like to deposit?"))
                    print(f"Okay, you have deposited ${deposit}.")
                else:
                    print("Have a good day!")
            else:
                print("Have a good day!")
        else:
            print("Alright, please pick another option.")
        

    #user chooses to exit program/option 3
    elif user_choice == 3:
        print("Exiting the program, thank you for visiting!")
        in_use = False
    #Input not valid
    else:
        print("Sorry, that wasn't a valid option, please choose again.")
    #Returns if the code should run again
    return in_use

while loop_program:
    options()
    loop_program = user_selection()


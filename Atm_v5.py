pin = 1234
attempt = 3
a = False

balance = 1000
history = []

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount2):
    return balance - amount2

try:
    while True:
        password = int(input("Enter your PIN:\n: "))

        if password == pin:
            print("Moving to the main menu...")
            a = True
            break

        else:
            attempt = attempt - 1

            if attempt < 1:
                print("No more attempts left.")
                break

            print("Wrong PIN!!!")
            print(f"You've got {attempt} attempts left")

except ValueError:
    print("Wrong input. Please enter numbers only.")

if a:
    while True:
        try:
            main = input(
                "1. Balance\n"
                "2. Deposit\n"
                "3. Withdraw\n"
                "4. Exit\n"
                "5. History\n"
                "6. change_pin\n"
                "7. show details\n:"
            )

            if main == "4":
                print("Thanks for using our ATM")
                break

            elif main == "6":
                print("to change password!!")
                change = int(input("enter your old password:"))

                if change == pin:
                    new_pin = int(input("enter your new password :"))
                    pin = new_pin
                else:
                    print("incorrect password")
                    break
                    
            elif main == "7":
                print("account holder: Mohd Athar")
                print(f"cuurent balance ${balance}")
                print(f"current pin {pin}")

            elif main == "2":
                amount = int(input("Enter your amount: "))
                if amount < 1:
                    print("invalid amount")
                    continue

                history.append(f"{amount} is deposited")
                balance = deposit(balance, amount)
                print(f"{amount} deposited in your account")
                print(f"${balance} is your current balance")

            elif main == "3":
                amount2 = int(input("Enter your amount: "))

                if amount2 > balance:
                    print("Insufficient balance")
                    continue

                elif amount2 < 1:
                    print("invalid amount")
                    continue

                history.append(f"{amount2} is withdrawn")
                balance = withdraw(balance, amount2)
                print(f"{amount2} withdrawn from your account")
                print(f"${balance} is your current balance")

            elif main == "1":
                print(f"${balance} is your current balance")

            elif main == "5":
                for i in history:
                    print(i)

            else:
                print("Invalid option")

        except ValueError:
            print("Invalid command")
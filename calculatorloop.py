running = True 

while running == True:
    n1 = int(input("enter your first number:"))
    n2 = int(input("enter your second number:"))
    choice = input("enter your operation choosing from all of these(*,+,-,**,//,/):")
    
    if choice == "*":
        print("result", n1 * n2)
    elif choice == "+":
        print("result", n1 + n2)
    elif choice == "-":
        print("result", n1 - n2)
    elif choice == "**":
        print("result", n1 ** n2)
    elif choice == "//":
        print("result", n1 // n2)
    elif choice == "/":
        print("result", n1 / n2)
    else:
        print("invalid operation") 
        
    user_input = input("do you want to continue(yes/no):")
    if user_input == "no":
        running = False

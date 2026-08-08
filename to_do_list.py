l = []

try:
    while True:
        user = input("1.add task\n2.remove task\n3.view task\n4.exit\n:")

        if user == "1":
            enter = input("enter your task\n:")
            l.append(enter)

        elif user == "3":
            for index, task in enumerate(l):
                print(f"index {index + 1} : {task}")

        elif user == "4":
            break

        elif user == "2":
            index = int(input("enter your task to remove\n:")) - 1
            l.remove(l[index])

except (IndexError, ValueError) as error:
    print("please put right index")
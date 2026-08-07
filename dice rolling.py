import random

a = ["1","2","3","4","5","6"]

b = "".join(a)

x = str(random.choice(b))

while True:
    main = input("random draw a number\n1.yes\n2.no exit\n:")
    if main == "1":
        print(x)
    else:
       print("thanks for using my code")
       break
    
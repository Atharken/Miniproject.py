# password generator and strength checker attempt 3
import string
import random

while True:

    upper = 0
    lower = 0
    number = 0
    symbol = 0

    h0 = int(input("how many alphabet case you want\n:"))
    h2 = int(input("how many numbers you want\n:"))
    h3 = int(input("how many symbols you want\n:"))

    h = h0 + h2 + h3

    x = string.ascii_letters
    x2 = random.sample(x, h0)
    x3 = "".join(x2)

    y = string.digits
    y2 = random.sample(y, h2)
    y3 = "".join(y2)

    z = string.punctuation
    z2 = random.sample(z, h3)
    z3 = "".join(z2)

    a = x3 + y3 + z3

    a2 = random.sample(a, h)
    a3 = "".join(a2)

    print(a3)

    for i in a3:

        if i.isupper():
            print(f"{i} is uppercase")
            upper += 1

        elif i.islower():
            print(f"{i} is lowercase")
            lower += 1

        elif i.isdigit():
            print(f"{i} is number")
            number += 1

        elif i in string.punctuation:
            print(f"{i} is punctuation")
            symbol += 1

    if upper > 0 and lower > 0 and number > 0 and symbol > 0:
        print("your password is very strong")

    elif upper > 0 and lower > 0 and number > 0:
        print("password is strong")

    elif upper > 0 and lower > 0:
        print("password is a bit strong")

    elif upper > 0:
        print("password")
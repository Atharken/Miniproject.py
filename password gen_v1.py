# password generator and streanght checker
import string
import random

upper = 0
lower = 0
number = 0
symbol = 0


x = string.ascii_letters
x2 = random.sample(x,5) # random alphabet generation and convert list to string data
x3 = "".join(x2)

y = string.digits
y2 = random.sample(y,4) # random number generation and convert list to string data
y3 = "".join(y2)

z = string.punctuation
z2 = random.sample(z,4) # random symbols generation and convert list to string data
z3 = "".join(z2)

a = x3 + y3 +z3
while True:
  upper = 0
  lower = 0
  number = 0
  symbol = 0
  h = int(input("enetr your lenght of password between 8-13 you want to generates\n:"))
  if h < 8:
    break
  elif h > 13:
    break

  a2 = random.sample(a,h)
  a3 = "".join(a2)
  print(a3)
  for i in a3:
  #if a3.isupper() and a3.islower() and a3.isdigit() and a3.isspace():
    #print("password is strong")
    if i.isupper():  #new topics isupper/lower etc
      print(f"{i} is uppercase") 
      upper += 1
    elif i.islower():
      print(f"{i} is lowercase") 
      lower += 1
    elif i.isdigit():
      print(f"{i} is number")
      number += 1 
    elif i in string.punctuation:
      print(f"{i} is puntuation")
      symbol += 1
      
  if upper > 0 and lower > 0 and number > 0 and symbol > 0:
        print("your password is very strong")
  elif upper > 0 and lower > 0 and number > 0:
        print("password is strong")
  elif upper > 0 and lower > 0:
        print("password is a bit strong")
  elif upper > 0:
       print("password")# new topic and never studied about this yet so useful thanks to google
   
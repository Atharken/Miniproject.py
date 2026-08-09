import random

x = random.randint(1, 100)
attempt = 0
try:
  while True:

      main = int(input("enter your number\ntype 0 to leave\n:"))

      if main == x:
          print(f"your guess is correct {x}")
          print(f"you took {attempt} attempts ")
          break
      elif main == 0:
          print("thanks for using our code")
          print(f"you took {attempt} attempts ")
          break
          
      elif main > x:
          print("too high!!!")
          attempt += 1
      elif main < x:
          print("too low!!!")
          attempt += 1
except ValueError:
    print("invalid input")
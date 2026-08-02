#kbc system
points = 0
print("welcome to quiz mania")
user_input = input("to register input yes/no:")
if user_input == "yes":
     print("you've been selected for quiz mania")
     print("enter your name:")
     name = input("")
     print("hellow",name)
     print("question 1 which protramming lang is widely used for ai/ml")
    answer1 = input("1.java   2.c  3.python  4.html")
     if answer1 == 3:
            points = 0 + 1 
         
elif user_input == "no":
         print("Thanks for visiting quiz mania")
         
print(points)
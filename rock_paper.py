import random

l = ["rock","paper","scissors"]


score = 0
score2 = 0

try:

  while True:
    
      user_input = input("choose one of these\n1.rock\n2.paper\n3.scissors\n4.exit\n:")
      if user_input == "4":
           print(f"your score{score} computer score{score2}")  
           break
      computer = random.choice(l)
      user_choice = int(user_input) -1  #string to integer conversion
      if user_choice >= 3:
          print("error")
          continue
      elif user_choice <= -1:
          print("error")
          continue
      x = l[user_choice]
      print(f"your score{score} computer score{score2}")
      if x == computer:
          print("draw")
    
      elif x == "rock" and computer == "scissors":   # i didnt know that we can use if elif condition with and.
          print("you won")
          score = score + 1
       
      elif x == "paper" and computer == "rock":
          print("you won")
          score = score + 1        
      elif x == "scissors" and computer == "paper":
          print("you won")
          score = score + 1
          
      else:
          print("you lost")
          score2 = score2 + 1 
except ValueError:
    print("wrong input!!")
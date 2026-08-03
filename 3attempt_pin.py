pin = 1234

attempt = 3

try:
  
 while True:

     password = int(input("enter your pin \n :"))

     if password == pin: 
       print("moving to the main menu....")
       break
   
     elif password != pin:
       attempt = attempt - 1 
       if attempt < 1:
            print("no more attmpt is left")
            break
       print("wrong pin!!!")
       print(f"you've got {attempt} attempts left")
      
except ValueError: 
      print("wrong input please enter your numbers")
    
      
    

balance = int(1000) 
history = []
def deposit(balance,amount):
       return(balance + amount)
def withdraw(balance,amount2):
       return(balance - amount2)
while True:
  try:
    main = str(input("1.balance  2.deposit  3.withdraw  4.exit 5.history :"))
    if main == "4":
      print("thanks for using our atm")
      break 
    elif main == "2":
      amount = int(input("enter your amount :"))
      history.append(f"{amount} is deposited")
      balance = deposit(balance,amount)
      print(f"{amount} deposited in your account")
    elif main == "3":
      amount2 = int(input("enter your amount :"))
      history.append(f"{amount2} is withdrawn")
      if amount2 > balance:
         print("insufficient balance")
         continue
      balance = withdraw(balance,amount2)
      print(f"{amount2} withdrawed in your account")
    elif main == "1":
      print(balance)
    elif main == "5":
       for i in history:
          print(i)
    else:
       print("invalid option")
  except ValueError:
     print("invalid command")
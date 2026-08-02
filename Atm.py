balance = int(1000) 
def deposit(a):
       return(balance + a)
def withdraw(b):
       return(balance - b)
while True:
  try:
    main = str(input("1.balance  2.deposit  3.withdraw  4.exit :"))
    if main == "4":
      print("thanks for using our atm")
      break 
    elif main == "2":
      amount = int(input("enter your amount :"))
      balance = deposit(amount)
      print(f"{amount} deposited in your account")
    elif main == "3":
      amount2 = int(input("enter your amount :"))
      if amount2 > balance:
         print("insufficient balance")
         continue
      balance = withdraw(amount2)
      print(f"{amount2} withdrawed in your account")
    elif main == "1":
      print(balance)
    else:
       print("invalid option")
  except ValueError:
     print("invalid command")
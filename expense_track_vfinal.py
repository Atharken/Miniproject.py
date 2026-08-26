#l = [{"name" : "kk","amount" : 1000,"category" : "music"},{"name" : "arjit","amount" : 1000,"category" : "music"},{"name" : "milk","amount" : 100,"category" : "grocery"}] 
l = []
file = open("expense.txt","r")
for i in file:
   data = [x.strip()for x in i.strip().split("|")] # this program converts string data remove spaces from beggining and end then split every word. also remove spaces again and make a list out of string data.
   expense = {"name" : data[0],"amount" : int(data[1]),"category" : data[2]}  #make a dictionary out of string to list conversion we did stored in variable data using index value.
   l.append(expense) #add dictionary to the list veriable l .
file.close()     
       

while True:
  
    main = input("1.add expense\n2.view expense\n3.calculate total\n4.search by category\n5.remove expense\n6.exit\n:")

    if main == "1":
        name = input("name:")
        try:
          amount = int(input("amount:"))
        except ValueError:
            print("wrong input !!!")
            continue   
        if amount < 1:
            print("invalid amount")
            continue 
        category = input("category:")
        expense = {
           "name" : name,
           "amount" : amount,
           "category" : category
        }
        l.append(expense)
        file = open("expense.txt","a")
        # at this part we are storing our expense data into our code variable list l then we are also adding these data to expense.txt for future use as string data. 
        file.write(f"{name} | {amount} | {category}\n")
        file.close()
        
      
    elif main == "2":
        for index, value in enumerate(l):
          print(f"index {index + 1} : {value['name']} | {value['amount']} | {value['category']}")
    elif main == "3":
        total = 0
        for i in (l):
            total = total + i["amount"]
        print(f"your total expense is ${total}")
    elif main == "4":
        found = False
        main2 = input("enetr your category\n:")
        for i in (l):
            if i["category"] == main2:
              print(f"{i['name']} | {i['amount']} | {i['category']}")
              found = True
        if found == False:
          print(f"theres no {main2} category") 
    elif main == "5":
       main3 = input("enter your expense category\n:")
       found = False

       for key, value in enumerate(l):
          if value["category"] == main3:
             print(f"{key + 1}  {value}")
             found = True


       if found == False:
          print(f"theres no such category as {main3}")
          continue
              

       try:
          remove = int(input("enter the sequence number of your item\n:"))
          removeon = l.pop(remove - 1)
          print(f"removed : {removeon}")
       except (ValueError,IndexError):
            print("invalid input")
            continue
     
       file = open("expense.txt","w")
       for x in l:
         file.write(f"{x["name"]} | {x["amount"]} | {x["category"]}\n")
       file.close()
       
    


        
       


                
    elif main == "6":
        print("thanks for using our code")
        break
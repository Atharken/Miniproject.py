l = [{"name" : "kk","amount" : 1000,"category" : "music"},{"name" : "arjit","amount" : 1000,"category" : "music"},{"name" : "milk","amount" : 100,"category" : "grocery"}] 

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
        expense = {"name" : name,"amount" : amount,"category" : category}
        l.append(expense)
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
       for key, value in enumerate(l):
          if value["category"] == main3:
             print(f"{key + 1}  {value}")
       remove = int(input("enter the sequence number of your item\n:"))
       removeon = l.pop(remove - 1)
                
    elif main == "6":
        print("thanks for using our code")
        break
l = [{"name" : "kk","amount" : 1000,"category" : "music"},{"name" : "arjit","amount" : 1000,"category" : "music"}]

while True:
    main = input("1.add expense\n2.view expense\n3.calculate total\n4.search by category\n5.exit\n:")

    if main == "1":
        name = input("name:")
        amount = int(input("amount:"))
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
        main2 = input("enetr your category\n:")
        for i in (l):
            if i["category"] == main2:
              #for index, value in enumerate(l):
              print(f"{i['name']} | {i['amount']} | {i['category']}")
    elif main == "5":
        print("thanks for using our code")
        break
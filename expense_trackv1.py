l = [{"name": "milk", "amount": 100, "category": "grocery"}]

while True:
    main = input("1.add expense\n2.view expense\n3.calculate total\n4.search by category\n5.exit\n:")

    if main == "1":
        name = input("name:")
        amount = int(input("amount:"))

        if amount < 1:
            print("invalid amount")
            continue

        category = input("category:")
        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }
        l.append(expense)

    elif main == "2":
        for key, value in enumerate(l):
            print(f"index {key + 1}: {value['name']} | {value['amount']} | {value['category']}")
            
            #only add expense and view is working not getting enough time 🥲 for coding because of collage.
            #need to bunk more classes 
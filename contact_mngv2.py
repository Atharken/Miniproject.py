x = {'atharken' :'9310455555','hhhhh' : '67747778'}

try:
  while True:

     main = input("1.addd contact\n2.remove contact\n3.view contacts\n4.search contact by name\n5.exit\n:")

     if main == "1":
        number = input("enter your contact\n:")
        if number in x.values():
         print("contact already existed in directory")
         continue
        if number.isdigit():
            key = input("add name of the contact\n:")
            if key in x:
               print("contact already existed in directory")
               continue
            
            x[key] = number
        else:
           print("only numeric value is aplicable for contacts!!")
           continue
        #key = input("add name of the contact\n:")
        #x[key] = number
     elif main == "3":
        for index,(key, value) in enumerate(x.items()):
          print(f" {index + 1} name:{key}: contact:{value}")
     elif main == "2":
        for index,(key, value) in enumerate(x.items()):
                 print(f" {index + 1} name:{key}: contact:{value}")
        main2 = int(input("which contact you want to remove?\n"))
        main2 = main2 - 1
        y = list(x.keys())[main2]   # so the y is the veriable whos holding the dictionary which i converted into list just now 
        x.pop(y)
     elif main == "4":
        main3 = input("enter name of contact\n:")
        print(x[main3])
     elif main == "5":
        print("thanks for using my code")
        break
except ValueError:
  print("error")
except (IndexError, KeyError):
  print("The requested item could not be found.")
class library:

    
    def __init__(self):
      self.books = []
    
    def add(self, book):
       self.books.append(book)
    def num_books(self):
       return len(self.books)

       
y = library() # if it is in a loop it will always generate a new list and remove old list. calling a class outside loop. it became self.books


while True:


  x = input("enter name of the book\n:")


  if x == "exit":
     for i,j in enumerate(y.books, 1):
       print(i,j)
     print(f"number of books in library : {y.num_books()}")
     break

  y.add(x) # adds input data into list self.books
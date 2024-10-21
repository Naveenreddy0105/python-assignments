'''6.Create an abstract class LibraryItem with abstract methods borrow() and return_item().
 Then create two subclasses:

Book, with attributes title, author, and num_copies.
DVD, with attributes title, director, and duration.
Implement a function borrow_item(item) that borrows the library item and 
decreases the number of available copies (for books) or marks the DVD as borrowed.'''

from abc import ABC

class LibraryItem(ABC):
    def borrow(self):
        pass
    def return_item(self):
        pass

class Book(LibraryItem):
    def __init__(self,title,author,num_copies):
        self.title = title
        self.author =author
        self.num_copies= num_copies
    def borrow(self):
        if self.num_copies>0:
            self.num_copies -= 1
            print(f"Borrowing book:{self.title} by {self.author}.copies left:{self.num_copies}")

class DVD (LibraryItem):
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        self.borrowed = False
    def borrow(self):
        if not self.borrowed == True:
            print(f"Borrowing DVD:{self.title} is directed by {self.director}.Duration:{self.duration} in minutes.")
        else:
            print(f"Sorry,{self.title} is currently borrowed.")
    def return_item(self) :
        if self.borrowed != False :
            print(f"Returned DVD:{self.title}.Now avaiable")
        else:
            print(f"{self.title}was not borrowed.")

def borrow_item(item:LibraryItem):item.borrow()
book = Book("1995","The real solider",3)
dvd = DVD("Darling","maruthi",150)

borrow_item(book)
borrow_item(book)
borrow_item(book)
borrow_item(book)
borrow_item(dvd)
borrow_item(dvd)
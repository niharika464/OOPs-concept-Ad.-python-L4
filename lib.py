class Library:
    def __init__(self,books):
        self.books=books
        print (....Welcome to the Library....)
    def display_books(self):
        print("\n Book available in the Library:")
        for book in self.books:
            print(f"-{book}") #print(book)
        print()

    def lend_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"You have borrowed {book}...Enjoy your reading with new explorations....")
        else:
            print(f"Sorry ,{book} is not available currently...")

    def return_book(self,book):
        self.books.append(book)
        print(f"Thankyou for returning {book} book on time....")

    def add_book(self,book):
        self.books.append(book)
        print(f"The new book {book} is added...")

    def __del__(self):
        print("Thankyou for visiting our library....have a nice day...Byee...")

l=Library(["Sapiens", "Romeo and Juliet", "I am divine.So are you", "My Favourite sister"])

l.display_books()

l.lend_book("Sapiens")
l.lend_book("Sapiens")
l.return_book("Sapiens")
l.add_book("Harry potter")
l.display_book()
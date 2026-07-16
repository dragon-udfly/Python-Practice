"""A custom module for book blueprint"""

class Book:
    """Class for Book blueprint"""
    def __init__(self, title, author, category, is_borrowed, price = 0.0):
        self.__title = title 
        self.__author = author 
        self.__category = category 
        self.__is_borrowed = is_borrowed
        self.__price = price 

    @property 
    def title(self):
        """Return title"""
        return self.__title 
    
    @property 
    def author(self):
        """Return author"""
        return self.__author
    
    @property 
    def price(self):
        """Return price"""
        return self.price
    
    @property 
    def category(self):
        """Return category"""
        return self.category 
    
    @property 
    def is_borrowed(self):
        """Return whether borrowed or not"""
        return self.__is_borrowed
    
    @price.setter 
    def price(self, price):
        """Change price"""
        self.__price = price 

    @is_borrowed.setter 
    def is_borrowed(self, is_borrowed):
        """Change borrowed state"""
        self.__is_borrowed = is_borrowed

    def print_book(self):
        print(f"Title: {self.__title}\nCategory: {self.__category}\nAuthor: {self.__author}\nPrice: ${self.__price}\n")

if __name__ == "__main__":
    print("Book Class.")
    book = Book("Any Title", "Any Author", "Any Category", False, 32.3)
    book.print_book()

# All setters should raise Exception upon failure
# All classes should also keep track of all members using a class variable


# Create a Book class that has the following attributes: title (string)
class Book:
    # All classes should also keep track of all members using a class variable
    all = []
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
            Book.all.append(self)
        else:
            raise Exception("invalid Title")

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


# Create an Author class that has the following attributes: name (string)
class Author:
    # All classes should also keep track of all members using a class variable
    all = []    
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
            self._contracts = []
            Author.all.append(self)
  
    
    # contracts(self): This method should return a list of related contracts
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    # books(self): This method should return a list of related books using the Contract class as an intermediary
    def books(self):
        return [contract.book for contract in self.contracts()]

    # sign_contract(book, date, royalties): This method should create and return a new Contract object between the author and the specified book with the specified date and royalties
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)  
    
    # total_royalties(): This method should return the total amount of royalties that the author has earned from all of their contracts
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    
    # @classmethod
    # def contracts_by_date(cls):
    #     return sorted(Contract.all, key=lambda contract: contract.date)


# Create a Contract class that has the following properties: 
#   author (Author object), 
#   book (Book object), 
#   date (string),
#   royalties (int)
class Contract:
    # All classes should also keep track of all members using a class variable
    all = []    
    def __init__(self, author, book, date, royalties):

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
        
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Invalid author")
        self._author = value


    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Invalid book")
        self._book = value


    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Invalid date")
        self._date = value    


    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Invalid royalties")
        self._royalties = value   

    # A class method contracts_by_date(cls, date): This method should return all contracts that have the same date as the date passed into the method.
    
    @classmethod
    def contracts_by_date(cls):
        return sorted(Contract.all, key=lambda contract: contract.date)
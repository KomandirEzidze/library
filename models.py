import datetime

class Book():
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.datePublished = date
        self.borrowed = None
        self.dateBorrow = None
        self.dateReturn = None

    def borrow(self, borrowed):
        self.borrowed = borrowed
        self.dateBorrow = datetime.date.today()
        self.dateBorrow = datetime.date.today() \
                            + datetime.timedelta(weeks=2)

    def __str__(self):
        return '{}\t{}\t{}'.format(self.title, self.author, self.datePublished)


class People():
    def __init__(self, name, date):
        self.name = name
        self.dateBirth = date
        self.books = list()

    def addBook(self, book):
        self.books.append(book)

    def delBook(self):
        self.books.pop()

    def __str__(self):
        return '{}\t{}'.format(self.name, self.dateBirth)

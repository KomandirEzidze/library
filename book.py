import datetime

class Book():
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.datePublished = date
        self.borrowed = ''
        self.dateBorrow = None
        self.dateReturn = None

    def borrow(self, borrowed):
        self.borrowed = borrowed
        self.dateBorrow = datetime.date.today()
        self.dateBorrow = datetime.date.today() \
                            + datetime.timedelta(weeks=2)

    def __str__(self):
        pass

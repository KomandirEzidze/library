from book import Book

def menu():
    print("Выберите один из пунктов меню\n" + \
           "1. Добавить книгу\n" + \
           "2. Взять книгу\n" + \
           "Введите q, чтобы выйти.")

def choice():
    for (i, book) in enumerate(books):
        #Должно отображать номер, название, автора, дату публикации
        #через знаки табулиции 
        print('{}\t{}'.format(str(i), book))
    ch = int(input('Введите номер книги: '))
    return ch

def addBook():
    title = input('Название книги: ')
    author = input('Автор книги: ')
    date = input('Дата публикации: ')
    book = Book(title, author, date)
    books.append(book)

def borrowBook():
    name = input('Введите имя заемщика: ')
    book = books[choice()]

books = list()

ch = ''
while (ch != 'q'):
    menu()
    ch = input('Ваш выбор: ')
    if (ch=='1'):
        addBook()
    elif (ch=='2'):
        borrowBook()

from models import Book, People

def menu():
    print("Выберите один из пунктов меню\n" + \
           "1. Добавить книгу\n" + \
           "2. Взять книгу\n" + \
           "3. Показать все книги\n" + \
           "4. Добавить читателя\n" + \
           "5. Показать взятые книги\n" + \
           "6. Показать читателей\n" + \
           "7. Показать книги в наличии\n" + \
           "Введите q, чтобы выйти.")

def choiceBook():
    showNotBorrow()
    ch = int(input('Введите номер книги: '))
    return ch

def addBook():
    title = input('Название книги: ')
    author = input('Автор книги: ')
    date = input('Дата публикации: ')
    book = Book(title, author, date)
    books.append(book)

def showPeople():
    for (i, people) in  enumerate(peoples):
        print('{}\t{}'.format(str(i), people))

def choicePeople():
    '''Выводит список людей и надо выбрать из него одного,
        возвращает экземпляр класса People(т.е человека)'''
    showPeople()
    ch = int(input('Введите номер читателя: '))
    return peoples[ch]

def borrowBook():
    book = books[choiceBook()]
    reader = choicePeople()
    book.borrow(reader)
    reader.addBook(book)

def showBook(ch):
    for (i, book) in  enumerate(books):
        if ch=='3':
            print('{}\t{}'.format(str(i), book))
        elif ch=='5':
            if (book.borrowed != None):
                print('{}\t{}'.format(str(i), book))
        elif ch=='7':
            if (book.borrowed == None):
                print('{}\t{}'.format(str(i), book))

def addPeople():
    name = input('Введите имя человека: ')
    date = input('Введите дату рождения: ')
    people = People(name, date)
    peoples.append(people)

books = list()
peoples = list()

ch = ''
while (ch != 'q'):
    menu()
    ch = input('Ваш выбор: ')
    if (ch=='1'):
        addBook()
    elif (ch=='2'):
        borrowBook()
    elif (ch=='3' or ch=='5' or ch=='7'):
        showBook(ch)
    elif (ch=='4'):
        addPeople()
    elif (ch=='6'):
        showPeople()

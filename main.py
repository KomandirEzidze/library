from models import Book, People

def menu():
    print("Выберите один из пунктов меню\n" + \
           "1. Добавить книгу\n" + \
           "2. Взять книгу\n" + \
           "3. Показать все книги\n" + \
           "4. Добавить читателя\n" + \
           "5. Показать взятые книги\n" + \
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
    '''Выводит список читателей'''
    pass

def choicePeople():
    '''Выводит список людей и надо выбрать из него одного,
        возвращает экземпляр класса People(т.е человека)'''
    pass

def borrowBook(): # Переделать
    name = input('Введите имя заемщика: ') # Теперь у нас человек объект
    book = books[choiceBook()]
    book.borrow(name)
    # Добавить книгу читателю

def showBook():                                     #
    for (i, book) in  enumerate(books):         #
        print('{}\t{}'.format(str(i), book))    #
                                                #
def showBorrow():                               #
    for (i, book) in  enumerate(books):         #
        if (book.borrowed != None):             #
            print('{}\t{}'.format(str(i), book))#
                                                #
def showNotBorrow():                            #
    for (i, book) in  enumerate(books):         #
        if (book.borrowed == None):             #
            print('{}\t{}'.format(str(i), book))#

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
    elif (ch=='3'):
        showBook()
    elif (ch=='4'):
        addPeople()
    elif (ch=='5'):
        showBorrow()

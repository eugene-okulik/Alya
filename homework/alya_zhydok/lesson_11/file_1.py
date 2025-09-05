class Book:
    material_pages = 'бумага'
    text = 'ru'

    def __init__(self, title, author, num_pages, isbn, reserved):

        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = reserved


book1 = Book("Идиот", "Достоевский", 500, "978-5-17-123456-7", False)
book2 = Book("Машина времени", "Герберт Уэллс", 250, "978-5-17-654321-0", False)
book3 = Book("Война и мир", "Толстой", 1000, "978-5-17-112233-4", False)
book4 = Book("История России", "Петров", 300, "978-5-17-445566-8", False)
book5 = Book("Тайна", "Некто", 150, "978-5-17-778899-0", False)

book3.reserved = True

for b in [book1, book2, book3, book4, book5]:
    if b.reserved:
        print(f"Название: {b.title}, Автор: {b.author}, страниц: {b.num_pages}, "
              f"материал: {b.material_pages}, зарезервирована")
    else:
        print(f"Название: {b.title}, Автор: {b.author}, страниц: {b.num_pages}, материал: {b.material_pages}")


class SchoolTextbook(Book):
    def __init__(self, title, author, num_pages, isbn, reserved, subject, grade, has_exercise):
        super().__init__(title, author, num_pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_exercise = has_exercise


textbook1 = SchoolTextbook("Алгебра", "Иванов", 200, "978-5-17-444444-4", False, "Математика", 9, True)
textbook2 = SchoolTextbook("История России", "Петров", 180, "978-5-17-555555-5", False, "История", 10, False)
textbook3 = SchoolTextbook("География", "Сидоров", 150, "978-5-17-666666-6", False, "География", 8, True)

textbook2.reserved = True

for t in [textbook1, textbook2, textbook3]:
    if t.reserved:
        print(f"Название: {t.title}, Автор: {t.author}, страниц: {t.num_pages}, "
              f"предмет: {t.subject}, класс: {t.grade}, зарезервирована")
    else:
        print(f"Название: {t.title}, Автор: {t.author}, страниц: {t.num_pages}, "
              f"предмет: {t.subject}, класс: {t.grade}")

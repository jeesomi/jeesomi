class Library:
   
    def __init__(self):
        self.books = [] 
    
    def add_book(self, title, author):
    
        book = {
            'title': title,
            'author': author
        }
        self.books.append(book)
        print(f"کتاب '{title}' توسط {author} اضافه شد.")
    
    def remove_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                print(f"کتاب '{title}' حذف شد.")
                return True
        
        print(f"کتاب با عنوان '{title}' یافت نشد.")
        return False
    
    def search_book(self, title):
        for book in self.books:
            if book['title'] == title:
                print(f"کتاب یافت شد: '{book['title']}' توسط {book['author']}")
                return book
        
        print(f"کتاب '{title}' یافت نشد.")
        return None
    
    def show_books(self):
        if not self.books:
            print("کتابخانه خالی است.")
        else:
            print("کتاب‌های موجود در کتابخانه:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. '{book['title']}' - {book['author']}")
        
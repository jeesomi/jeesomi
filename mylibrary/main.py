from library import Library

def main():
    library = Library()
    
    print("سیستم مدیریت کتابخانه")
    print("=" * 30)
    
   
    while True:
        print("\nمنو:")
        print("1. نمایش کتاب‌ها")
        print("2. اضافه کردن کتاب")
        print("3. حذف کتاب")
        print("4. جستجوی کتاب")
        print("5. خروج")
        
        choice = input("لطفاً عدد مورد نظر را انتخاب کنید: ")
        
        if choice == "1":
            library.show_books()
        
        elif choice == "2":
            title = input("عنوان کتاب: ")
            author = input("نویسنده کتاب: ")
            library.add_book(title, author)
        
        elif choice == "3":
            title = input("عنوان کتاب برای حذف: ")
            library.remove_book(title)
        
        elif choice == "4":
            title = input("عنوان کتاب برای جستجو: ")
            library.search_book(title)
        
        elif choice == "5":
            print("خروج از برنامه...")
            break
        
        else:
            print("گزینه نامعتبر!")


if __name__ == "__main__":
    main()
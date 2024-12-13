import save_all_books
import save_lends
from datetime import datetime

def lend_book(all_books, all_lends):
    book_title = input("Enter the book title to lend: ")
    for book in all_books:
        if book["title"] == book_title:
            if book["quantity"] > 0:
                borrower_name = input("Enter Borrower's Name: ")
                phone_number = input("Enter Borrower's Phone Number: ")
                due_date = input("Enter Return Due Date (DD-MM-YYYY): ")

                book["quantity"] -= 1
                lend_info = {
                    "borrower_name": borrower_name,
                    "phone_number": phone_number,
                    "book_title": book_title,
                    "due_date": due_date,
                    "lend_date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                }

                all_lends.append(lend_info)
                save_all_books.save_all_books(all_books)
                save_lends.save_lends(all_lends)
                
                print("Book lent successfully!")
                return all_books, all_lends
            else:
                print("There are not enough books available to lend.")
                return all_books, all_lends

    print("Book not found.")
    return all_books, all_lends

import save_all_books
import save_lends

def return_book(all_books, all_lends):
    book_title = input("Enter the book title to return: ")
    borrower_name = input("Enter Borrower's Name: ")
    
    for lend in all_lends:
        if lend["book_title"] == book_title and lend["borrower_name"] == borrower_name:
            for book in all_books:
                if book["title"] == book_title:
                    book["quantity"] += 1
                    all_lends.remove(lend)
                    save_all_books.save_all_books(all_books)
                    save_lends.save_lends(all_lends)
                    
                    print("Book returned successfully!")
                    return all_books, all_lends

    print("No matching lend record found.")
    return all_books, all_lends

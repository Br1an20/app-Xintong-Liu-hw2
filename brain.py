from books import BooksDocument, Books
from borrowers import BorrowersDocument, Borrowers
import time
import sys
from mongoengine.queryset.visitor import Q

def not_valid():
    print("Not a valid command.")

def db_to_book_list() -> [Books]:
    books = BooksDocument.objects
    result = []
    for book in books:
        result.append(Books(book.author, book.borrower_id, book.borrower_name, book.checked_out, book.book_id, book.title, book.pk))
    return result

# Convert db to the list type
def db_to_borrowers_list() -> [Borrowers]:
    borrowers = BorrowersDocument.objects
    result = []
    for borrower in borrowers:
        result.append(Borrowers(borrower.borrower_id, borrower.name, borrower.phone, borrower.pk))
    return result

# Update the changes to the db
def update_book_in_db(new_book: Books):
    the_doc = BooksDocument.objects(id=new_book.primary_key).first()
    the_doc.checked_out = new_book.checked_out
    the_doc.borrower_id = new_book.borrower_id
    the_doc.borrower_name = new_book.borrower_name
    the_doc.save()

def process_input(choice: str):
    book_list = db_to_book_list()
    borrowers_list = db_to_borrowers_list()
    borrowers_id = []
    borrowers_name = []
    books_id = []
    books_checked = []

    if choice == 'books':

        if len(book_list) > 0:
            for index, q in enumerate(book_list):
                print(f"[{index + 1}] {q}")

    elif choice == 'checkout':
        input_borrower_id = input("Enter your borrowerId: ")
        if len(borrowers_list) > 0:
            # Get borrower id and name from the db
            for borrower in borrowers_list:
                borrowers_id.append(borrower.borrower_id)
                borrowers_name.append(borrower.name)
            if input_borrower_id not in borrowers_id:
                print("Please enter right id!")
            else:
                input_book_id = input("Enter the bookId: ")
                for book in book_list:
                    # book_id and checked_out is from books.py
                    books_id.append(book.book_id)
                    books_checked.append(book.checked_out)

                # Check if the input book id is in the database
                if input_book_id not in books_id:
                    print("Please Enter the correct book id!")
                else:
                    for i in range(len(book_list)):
                        if book_list[i].book_id == input_book_id and book_list[i].checked_out == 'N':
                            book_list[i].checked_out = 'Y'
                            book_list[i].borrower_id = input_borrower_id
                            book_list[i].borrower_name = borrowers_name[borrowers_id.index(input_borrower_id)]
                            # Apply changes to the db
                            updated_book = Books(book_list[i].author, book_list[i].borrower_id,
                                                 book_list[i].borrower_name, book_list[i].checked_out,
                                                 book_list[i].book_id, book_list[i].title, book_list[i].primary_key)
                            update_book_in_db(updated_book)
                            print(f"{book_list[i].borrower_name} has checked out {book_list[i].title}")
                        elif book_list[i].book_id == input_book_id and book_list[i].checked_out == 'Y':
                            print(f"{input_book_id} is already checked out by someone.")

    elif choice == 'return':
        input_borrower_id = input("Enter your borrowId: ")
        for borrower in borrowers_list:
            borrowers_id.append(borrower.borrower_id)
            borrowers_name.append(borrower.name)
        if input_borrower_id not in borrowers_id:
            print(f"Borrower with id {input_borrower_id} does not exist")
        else:
            input_book_id = input("Enter book id : ")
            for book in book_list:
                # book_id and checked_out is from books.py
                books_id.append(book.book_id)
                books_checked.append(book.checked_out)

            # Check if the input book id is in the database
            if input_book_id not in books_id:
                print(f"Book with id {input_book_id} does not exist")
            else:
                for i in range(len(book_list)):
                    print(book_list[i].book_id)
                    if book_list[i].book_id == input_book_id and book_list[i].checked_out == 'Y':
                        print(f"{book_list[i].borrower_name} has returned {book_list[i].title}")
                        book_list[i].checked_out = 'N'
                        book_list[i].borrower_id = ''
                        book_list[i].borrower_name = ''
                        updated_book = Books(book_list[i].author, book_list[i].borrower_id,
                                             book_list[i].borrower_name, book_list[i].checked_out,
                                             book_list[i].book_id, book_list[i].title, book_list[i].primary_key)
                        update_book_in_db(updated_book)

                    elif book_list[i].book_id == input_book_id and book_list[i].checked_out == 'N':
                        print(f"{book_list[i].title} has not currently checked out.")

    elif choice == 'reset':
        for i in range(len(book_list)):
                book_list[i].checked_out = 'N'
                book_list[i].borrower_id = ''
                book_list[i].borrower_name = ''
                updated_book = Books(book_list[i].author, book_list[i].borrower_id,
                                     book_list[i].borrower_name, book_list[i].checked_out,
                                     book_list[i].book_id, book_list[i].title, book_list[i].primary_key)
                update_book_in_db(updated_book)
        print('Data has been reset')
    elif choice == 'exit':
        time.sleep(5)
        print('Exiting')
        time.sleep(5)
        sys.exit()
    else:
        not_valid()











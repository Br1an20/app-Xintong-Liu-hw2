from mongoengine import Document, StringField, ListField, IntField

class BooksDocument(Document):
    meta = {'collection': 'books'}
    author = StringField(max_length=200, required=True)
    borrower_id = StringField(max_length=200, required=True)
    borrower_name = StringField(max_length=200, required=True)
    checked_out = StringField(max_length=200, required=True)
    book_id = StringField(max_length=200, required=True)
    title = StringField(max_length=200, required=True)


class Books:
    primary_key: str
    author: str
    borrower_id: str
    borrower_name: str
    checked_out: str
    book_id: str
    title: str

    def __init__(self, author, borrower_id, borrower_name, checked_out, book_id, title, primary_key):
        self.author = author
        self.borrower_id = borrower_id
        self.borrower_name = borrower_name
        self.checked_out = checked_out
        self.book_id = book_id
        self.title = title
        self.primary_key = primary_key

    def set_primary_key(self, the_key):
        self.primary_key = the_key

    def get_author(self, the_author):
        self.author = the_author

    def get_borrower_id(self, the_borrower_id):
        self.borrower_id = the_borrower_id

    def get_borrower_name(self, the_borrower_name):
        self.borrower_name = the_borrower_name

    def get_book_id(self, the_book_id):
        self.book_id = the_book_id

    def get_checked_out(self, the_checked_out):
        self.checked_out = the_checked_out

    def get_title(self, the_title):
        self.title = the_title

    def __str__(self):
        result = str(self.book_id) + " " + "<" + str(self.title) + ">" + "," + str(self.author) + "," + str(self.checked_out) + "," + str(self.borrower_id) + "," + str(self.borrower_name)
        return result


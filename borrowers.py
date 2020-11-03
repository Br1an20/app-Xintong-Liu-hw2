from mongoengine import Document, StringField, ListField, IntField

class BorrowersDocument(Document):
    meta = {'collection': 'borrowers'}
    borrower_id = StringField(max_length=200, required=True)
    name = StringField(max_length=200, required=True)
    phone = StringField(max_length=200, required=True)


class Borrowers:
    primary_key: str
    borrower_id: str
    name: str
    phone: str


    def __init__(self, borrower_id, name, phone, primary_key):
        self.borrower_id = borrower_id
        self.name = name
        self.phone = phone
        self.primary_key = primary_key

    def set_primary_key(self, the_key):
        self.primary_key = the_key

    def get_borrower_id(self, the_borrower_id):
        self.borrower_id = the_borrower_id
    def get_name(self, the_name):
        self.name = the_name
    def get_phone(self,the_phone):
        self.phone = the_phone

    def __str__(self):
        result = str(self.borrower_id) + " " + str(self.name) + " " + str(self.phone)
        return result


from birthday import Birthday
from name import Name
from phone import Phone

class Record:
    def __init__(self, name): 
        self.name = Name(name) 
        self.phones = []
        self.birthday = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phone: {'; '.join(p.value for p in self.phones)}"
    
    # Method to add phone to record
    def add_phone(self, number: str): 
        self.phones.append(Phone(number))

    # Method to remove phone from record
    def remove_phone(self, number: str):
        self.phones = list(filter(lambda phone: phone == number, self.phones))

    # Method to edit phone in the record
    def edit_phone(self, old_number, new_number):
        self.phones = list(
            map(
                lambda phone: Phone(new_number) if phone.value == old_number else phone,
                self.phones,
            )
        )

    # Method to find phone in record
    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
    # Method to add birthday to record        
    def add_birthday(self, date):
        self.birthday = Birthday(date)
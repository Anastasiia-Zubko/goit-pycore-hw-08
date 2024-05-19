import pickle

from address_book import AddressBook

FILE_NAME = "addressbook.pkl"


def save_data(book, filename=FILE_NAME):
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename=FILE_NAME):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook() # Повернення нової адресної книги, якщо файл не знайдено
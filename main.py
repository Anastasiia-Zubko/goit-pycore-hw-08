from address_book import AddressBook
from record import Record
from file_storage import save_data, load_data

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            return str(error)
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_number, new_number = args
    record = book.find(name)
    if record is None:
        return "Record not found"
    else:
        record.edit_phone(old_number, new_number)
        return "Phone changed"

@input_error
def all_contacts(book: AddressBook):
    output = "Address book:"
    for record in book.data.values():
        output += f"\n{record}"
    return output

@input_error
def show_phone(args, book: AddressBook):       
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Record not found"
    return record

@input_error
def add_birthday(args, book):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add-birthday [name] [date]"
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added."
    else:
        return "Record not found"

@input_error
def show_birthday(args, book):
    if len(args) != 1:
        return "Invalid number of arguments. Usage: show-birthday [name]"
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday
        else:
            return "Birthday not added to this contact."
    else:
        return "Record not found"

@input_error
def birthdays(book):
    birthdays = book.get_upcoming_birthdays()
    output = "Upcoming birthdays:"
    for record in birthdays:
        output += f"\n{record}"
    return output


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(all_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args,book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
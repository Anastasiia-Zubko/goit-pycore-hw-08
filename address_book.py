from collections import UserDict
from datetime import datetime
from field import Field


class AddressBook(UserDict):
     # Method to add record to address book
    def add_record(self, record):
        self.data[record.name.value] = record

     # Method to edit record in address book
    def find(self, name):
        return self.data.get(name)

    # Method to delete record from address book
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        upcoming_birthdays =[] # empty list for upcoming birthdays 
        today = datetime.today().date() # get current date

        for name, record in self.data.items(): #  iterate through all the users
            if record.birthday is None: 
                continue
            birthday_this_year = record.birthday.value.date()
            birthday_this_year = birthday_this_year.replace(year=today.year)

            if birthday_this_year < today: # check if the birthday is in the past
                birthday_this_year = birthday_this_year.replace(year=today.year + 1) # add 1 year to the birthday
                
            days = birthday_this_year - today # calculate number of days between birthday and today

            if days.days <= 7: #check if the birthday is within the next 7 days 
                upcoming_birthdays.append({name: birthday_this_year.strftime("%Y-%m-%d")}) # add the birthday to upcoming_birthdays
            else:
                pass # ignore if its not within the next 7 days 
                
        if upcoming_birthdays: # check if there are upcoming birthdays  
            return upcoming_birthdays # return the birthday 
        else:
            return "No upcoming birthdays" # if there are no upcoming birthdays return "No upcoming birthdays"
            




        



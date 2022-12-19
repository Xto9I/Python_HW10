from collections import UserDict

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def change_record(self, record):
        self.data.update({record.name.value: record})

    def find_contact(self, name):
        for phone_name, numbers in self.data.items():
            if phone_name == name:
                return [number.value for number in numbers.phone_numbers]
        return "Contact not found!!!"


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone_numbers = []
    

    def add(self, phone):
        self.phone_numbers.append(Phone(phone))


    def change(self, phone, old_phone):
        self.delete(old_phone)
        self.add(phone)


    def delete(self, phone):
        for item in self.phone_numbers:
            if item == phone:
                del item
                return f"Number {Phone(phone)} deleted."
        return " Phone number not found!!! "    

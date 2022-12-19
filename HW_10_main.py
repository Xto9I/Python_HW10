import re
from HW_10_contact_book import Field, Record, AddressBook

contacts = AddressBook()  

def input_error(funk):
      
    def inner(*args,**kwargs):  

        try:
            return funk(*args,**kwargs)
        except KeyError: 
            return "This name does not exist."
        except IndexError:
            return "Did not receive a name or number."
        except:
            return "Option entered incorrectly."

    return inner

@input_error
def add(text):

    phone_number = get_phone(text)
    phone_name = get_name(text)
    record = Record(phone_name)
    record.add(phone_number)
    contacts.add_record(record)
    return "Number added. Something else?"

@input_error
def change(text):
    phone_number = get_phone(text)
    phone_name = get_name(text)
    for name, numbers in contacts.items():
        if name == phone_name:
            old_phone_number = [number.value for number in numbers.phone_numbers]
    record = Record(phone_name)
    record.change(phone_number, old_phone_number)
    contacts.change_record(record)
    result = f"{phone_name}\'s number {old_phone_number} changed to {phone_number}. Something else?"
    return result

@input_error
def delete(text):
    phone_number = get_phone(text)
    phone_name = get_name(text)
    record = Record(phone_name)
    record.delete(phone_number)

@input_error
def end(text):
    return "Good bye!"
    
#@input_error
def get_name(text):
    phone_name = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)[1].title()
    return phone_name

#@input_error
def get_phone(text):
    phone_number = re.findall(r"\d+", text)[-1]
    return phone_number

@input_error
def hello(text):
    return "How can I help you?"

@input_error
def phone(text):
    phone_name = get_name(text)
    return contacts.find_contact(phone_name)

@input_error
def show_all(text):
    result = []
    for phone_name, numbers in contacts.items():
        result.append(f"{phone_name} : {[number.value for number in numbers.phone_numbers]}")
    return result

def main():

    start = True

    while start:

        access = False
        entered_text = input()
        
        for key in user_command.keys():
            if bool(re.search(key, entered_text, flags=re.IGNORECASE)):
                
                access = True
                print(user_command[key](entered_text))

                if key in ["exit","good bye","close"]:
                    start = False  
                break
      
        if not access:
            print("Option entered incorrectly...")
               
      
user_command = {
    "add": add,
    "change": change,
    "delete": delete,
    "exit": end,
    "good bye": end,
    "close": end,
    "hello": hello,
    "phone": phone,
    "show all": show_all,
}


if __name__ == "__main__":
    main()

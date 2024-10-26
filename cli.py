from collections import UserDict

# Common class for fields
class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

# Class for name
class Name(Field):
		pass

# Class for phone with validation (10 numbers)
class Phone(Field):
    def __init__(self, value: str):
        # Validation of name
        if len(value) == 10 and all([el.isdigit() for el in value]):
            super().__init__(value)
        else:
            return 'Phone must contain 10 numbers'

# Class for record whoch contain name and list of Phones
class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones = []

    # Add phone to the record by taking phone, if phone is already exist return
    def add_phone(self, phone: str):
        if str(Phone(phone)) in self.phones:
            return 'Phone is already exist'
        self.phones.append(str(Phone(phone)))
        return self.phones
    
    # Remove phone from the record by taking phone, if phone not exist return
    def remove_phone(self, phone: str):
        if str(Phone(phone)) not in self.phones:
            return 'Phone is not in phones'
        self.phones = [el for el in self.phones if not el == str(Phone(phone))]
        return self.phones
    
    # Edit phone from the record by taking phone and new phone, if phone not exist return
    def edit_phone(self, phone: str, new_phone: str):
        if str(Phone(phone)) in self.phones:
            phone_index = self.phones.index(phone)
            self.phones.remove(phone)
            self.phones.insert(phone_index, new_phone)
            return self.phones
        else:
            return 'Phone is not in phones'

    # Find phone from the record by taking phone, if phone not exist return
    def find_phone(self, phone: str):
        if str(Phone(phone)) not in self.phones:
            return 'Phone is not in phones'
        return phone

    def __str__(self):
        return f'Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}'

# Class for address book
class AddressBook(UserDict):

    # Add record to the dict by taking record
    def add_record(self, record: Record):
        self.data[str(record.name)] = record.phones
        return self.data

    # Find record in dict by taking name
    def find(self, name: str):
        if name in self.data:
            return self.data[name]
        return 'No records with this name'
    
    # Delete record in dict by taking name, if name not exist return
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
            return self.data
        return 'No records with this name'
    


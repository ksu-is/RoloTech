class Contact:
    def whole(self, name, surname, number, email):
        self.name=name
        self.surname=surname
        self.number=number
        self.email=email
    def edit_name(self, name):
        self.name=name
        return self.name
    def edit_surname(self, surname):
        self.surname=surname
        return self.surname
    def edit_number(self, number):
        self.number=number
        return self.number
    def edit_email(self, email):
        self.email=email
        return self.email
    @classmethod
    def add(cls, name, surname, number, email):
        return cls(name, surname, number, email)
    @staticmethod
    def saved():
        print('CONTACTS SAVED: ', end='')
        for j, contact in enumerate(address_book):
            print(j, contact.name, end=' || ')
    @staticmethod
    def isempty(list):
        if len(list)==0
            print('No contact saved\n')
            return True
        return False
    def print_address_book(address_book):
    print('CONTACTS SAVED: ', end='')
    for j, contact in enumerate(address_book):
        print(j, contact.name, end=' || ')
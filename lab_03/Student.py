class Student:
    def __init__(self, name, phone, email, address):
        self._name = name
        self._phone = phone
        self._email = email
        self._address = address

    def modify(self, **kwargs):
        """Оновлює дані студента. Приймає ключові аргументи."""
        if 'name' in kwargs and kwargs['name']:
            self.set_name(kwargs['name'])
        if 'phone' in kwargs and kwargs['phone']:
            self.set_phone(kwargs['phone'])
        if 'email' in kwargs and kwargs['email']:
            self.set_email(kwargs['email'])
        if 'address' in kwargs and kwargs['address']:
            self.set_address(kwargs['address'])

    def details(self):
        """Повертає строкове представлення об'єкта."""
        return f"Name: {self._name}, Phone: {self._phone}, Email: {self._email}, Address: {self._address}"

    def get_name(self):
        return self._name

    def get_phone(self):
        return self._phone

    def get_email(self):
        return self._email

    def get_address(self):
        return self._address

    def set_name(self, value):
        if value:
            self._name = value

    def set_phone(self, value):
        if value:
            self._phone = value

    def set_email(self, value):
        if value:
            self._email = value

    def set_address(self, value):
        if value:
            self._address = value

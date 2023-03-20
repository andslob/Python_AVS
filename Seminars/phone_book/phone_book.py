class Contact:

    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def to_str(self):
        return f'{self.name}:{self.phone}:{self.comment}'

    def __str__(self):
        return f'{self.name:<20} | {self.phone:<20} | {self.comment:<20}'

class PhoneBook:
    def __init__(self, path: str):
        self.path = path
        self.phone_list = []
        self.open()

    def open(self):
        with open(self.path, 'r', encoding="UTF-8") as file:
            data = file.readlines()
        for contact in data:
            new_cont = contact.strip().split(':')
            self.phone_list.append(Contact(*new_cont))

    def save(self):
        data = '\n'.join([contact.to_str() for contact in self.phone_list])
        with open(self.path, 'w', encoding="UTF-8") as file:
            file.write(data)

    def __str__(self):
        result = ''
        for contact in self.phone_list:
            result += f'{contact}\n'
        return result[:-2]
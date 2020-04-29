class Person:
    def __init__(self, name, birthday_date):
        self.name = name
        self.birthday_date = birthday_date

    def __repr__(self):
        return f'Person: {self.name}'
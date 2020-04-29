from collections import Counter
from datetime import datetime, date
import json
from bokeh.plotting import figure, show, output_file

from person import Person


class Register:
    def __init__(self):
        self.people = []

    def load(self, filename):
        with open(f"{filename}", "r") as f:
            register_data = json.loads(f.read())

        for name, birthday_date in register_data.items():
            birthday_date = datetime.strptime(birthday_date, "%m/%d/%Y").date()
            person = Person(name, birthday_date)
            self.people.append(person)

        self.calculate_month_data()

    def check_birthday(self):
        name = input("Podaj imie i nazwisko naukowca: ")
        list_of_person = [person for person in self.people if name == person.name]
        if len(list_of_person) == 0:
            print(
                "Przepraszamy w bazie danych nie ma szukanej przez Ciebie informacji."
            )
        else:
            print(f"Podane imię i nazwisko znaleziono {len(list_of_person)} krotnie.")
            for person in list_of_person:
                print(person.birthday_date)

    def add(self):
        name = input("Podaj imię naukowca: ")
        while True:
            birthday_date = input("Podaj date urodzenia(MM/DD/RRRR): ")
            try:
                birthday_date = datetime.strptime(birthday_date, "%m/%d/%Y")
                break
            except:
                print("Podaj date w poprawnym formacie")

        person = Person(name, birthday_date)
        self.people.append(person)
        print(self.people)
        self.calculate_month_data()

    def save(self, filename):
        with open(f"{filename}", "w") as f:
            data_dict = {
                self.person.name: f"{self.person.birthday_date}"
                for self.person in self.people
            }
            json.dump(data_dict, f)

    def check_month(self):
        while True:
            month_name = input(
                "Podaj nazwę miesiąca w języku angielskim rozpoczynając od wielkiej litery: "
            )
            try:
                print(
                    f"Ilość naukowców urodzonych w miesiacu: {month_name} wynosi: {self.counter[month_name]}"
                )
            except:
                print(
                    "Niestety nie możemy wyświetlić odpowiedzi. Proszę sprawdź czy podałeś w odpowiedni sposób nazwę miesiąca."
                )

    def histogram(self, output_filname):
        output_file(output_filname)
        x_categories = []
        for number in range(1, 13):
            x_categories.append(date(2000, number, 1).strftime("%B"))
        x = [name_month for name_month in self.counter.keys()]
        y = [quantity for quantity in self.counter.values()]
        p = figure(x_range=x_categories)
        p.vbar(x=x, top=y, width=0.5)
        show(p)

    def calculate_month_data(self):
        list_of_months = [person.birthday_date.strftime("%B") for person in self.people]
        self.counter = Counter(list_of_months)

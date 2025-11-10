# Task 2
from datetime import datetime


class Passport:
    def __init__(
        self, number, name, surname, date_of_birth,
        place_of_birth, gender
    ):
        self.number = number
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.gender = gender

    def is_valid_age(self):
        now = datetime.now()
        year_diff = now.year - self.date_of_birth.year
        month_diff = now.month - self.date_of_birth.month
        day_diff = now.day - self.date_of_birth.day
        if year_diff < 18:
            return False
        if year_diff == 18 and month_diff < 0:
            return False
        if year_diff == 18 and month_diff == 0 and day_diff < 0:
            return False
        return True


class Visa:
    def __init__(self, number, date_of_issue,
                 date_of_expiration, country):
        self.number = number
        self.date_of_issue = date_of_issue
        self.date_of_expiration = date_of_expiration
        self.country = country


class ForeignPassport(Passport):
    def __init__(
        self, number, name, surname, date_of_birth,
        place_of_birth, gender,
        visas: list[Visa] = []
    ):
        super().__init__(
            number, name, surname, date_of_birth,
            place_of_birth, gender
        )
        self.visas = visas

    def add_visa(self, date_of_issue,
                 date_of_expiration, country):
        self.visas.append(Visa(
            number=len(self.visas) + 1,
            date_of_issue=date_of_issue,
            date_of_expiration=date_of_expiration,
            country=country
        ))

    def has_access(self, country):
        for visa in self.visas:
            if visa.country == country:
                return True
        return False


def can_buy_alcohol(passport):
    return passport.is_valid_age()


a = Passport(
    123456,
    "John", "Doe",
    date_of_birth="1990-01-01",
    place_of_birth="New York",
    gender="male"
)

foreign_passport = ForeignPassport(
    number=456789,
    visas=[
        Visa(
            number=1,
            date_of_issue="2022-01-01",
            date_of_expiration="2023-01-01",
            country="USA"
        )
    ]
)

passports = [
    a,
    foreign_passport.passport
]

for passport in passports:
    print(can_buy_alcohol(passport))

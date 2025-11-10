# Task 2
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
        return self.date_of_birth <= datetime.now() - '18 years'


class Visa:
    def __init__(self, number, date_of_issue,
                 date_of_expiration, country):
        self.number = number
        self.date_of_issue = date_of_issue
        self.date_of_expiration = date_of_expiration
        self.country = country


class ForeignPassport:
    def __init__(
        self, passport: Passport, number: int,
        visas: list[Visa] = []
    ):
        self.passport = passport
        self.number = number
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
    number=123456,
    name="John",
    surname="Doe",
    date_of_birth="1990-01-01",
    place_of_birth="New York",
    gender="male"
)

foreign_passport = ForeignPassport(
    passport=a,
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

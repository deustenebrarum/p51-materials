# Task 2
from abc import ABC, abstractmethod
from datetime import datetime


class Document(ABC):
    def __init__(self, number, name, surname):
        self.number = number
        self.name = name
        self.surname = surname

    @abstractmethod
    def is_valid(self):
        ...


class Passport(Document):
    def __init__(
        self, number, name, surname, date_of_birth,
        place_of_birth, gender
    ):
        super().__init__(number, name, surname)
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

    def is_valid(self):
        return self.number >= 10**9 and self.number < 10**10


class Visa:
    def __init__(self, number, date_of_issue,
                 date_of_expiration, country):
        self.number = number
        self.date_of_issue = date_of_issue
        self.date_of_expiration = date_of_expiration
        self.country = country

    def is_valid(self):
        return self.date_of_issue < self.date_of_expiration


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

    def is_valid(self):
        return (
            super().is_valid() and
            all([visa.is_valid() for visa in self.visas])
        )
        # Внутри работает так:
        # for visa in self.visas:
        #     if not visa.is_valid():
        #         return False
        # return True


class DriverLicense(Document):
    CATEGORIES = ("A", "B", "C", "D")

    def __init__(self, number, name, surname, categories):
        super().__init__(number, name, surname)
        self.categories = categories

    def is_valid(self):
        ...
        return all([
            category in DriverLicense.CATEGORIES
            for category in self.categories
        ])


def check_documents(documents: list[Document]):
    for document in documents:
        if not document.is_valid():
            print("Не прошла проверка документа: " +
                  f"{type(document).__name__}")
            return False
    return True


passport = Passport(
    2112_123456,
    "John", "Doe",
    date_of_birth=datetime(1990, 1, 1),
    place_of_birth="New York",
    gender="male"
)

foreign_passport = ForeignPassport(
    number=1221_12512,
    name="John",
    surname="Doe",
    date_of_birth=datetime(1990, 1, 1),
    place_of_birth="New York",
    gender="male",
    visas=[
        Visa(
            number=1,
            date_of_issue=datetime(2022, 1, 1),
            date_of_expiration=datetime(2023, 1, 1),
            country="USA"
        )
    ]
)

driver_license = DriverLicense(
    number=123456,
    name="John",
    surname="Doe",
    categories=["A", "B"]
)

document_pack: list[Document] = [
    passport,
    foreign_passport,
    driver_license,
    # если включить строгие подсказки,
    # добавление кода ниже даст ошибку
    # внутри vscode
    # хотя метод check_documents отработает правильно,
    # потому что использует только is_valid
    Visa(
        number=1,
        date_of_issue=datetime(2022, 1, 1),
        date_of_expiration=datetime(2023, 1, 1),
        country="USA"
    )
    # и тут стоит задуматься, о стоило ли вообще
    # какой-то конструктор относить к Document
    # может лучше, если он никакие поля нести не будет
    # от этого никому всё равно лучше не становится
    # код только сложнее
]

print(check_documents(document_pack))

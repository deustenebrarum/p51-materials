class Fraction:
    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def multiply(self, other):
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator)

    def divide(self, other):
        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator)

    def add(self, other):
        return Fraction(
            self.numerator * other.denominator +
            other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def sub(self, other):
        return Fraction(
            self.numerator * other.denominator -
            other.numerator * self.denominator,
            self.denominator * other.denominator
        )


class City:
    def __init__(self):
        self.name = ""
        self.region = ""
        self.country = ""
        self.population = 0
        self.postal_code = ""
        self.phone_code = ""

    def set_name(self, name):
        self.name = name

    def set_region(self, region):
        self.region = region

    def set_country(self, country):
        self.country = country

    def set_population(self, population):
        self.population = population

    def set_postal_code(self, postal_code):
        self.postal_code = postal_code

    def set_phone_code(self, phone_code):
        self.phone_code = phone_code

    def get_name(self):
        return self.name

    def get_region(self):
        return self.region

    def get_country(self):
        return self.country

    def get_population(self):
        return self.population

    def get_postal_code(self):
        return self.postal_code

    def get_phone_code(self):
        return self.phone_code

    def display_info(self):
        print(f"City: {self.name}")
        print(f"Region: {self.region}")
        print(f"Country: {self.country}")
        print(f"Population: {self.population}")
        print(f"Postal Code: {self.postal_code}")
        print(f"Phone Code: {self.phone_code}")

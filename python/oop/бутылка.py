from datetime import datetime, timedelta
import random


class BottleProduct:
    tax = 0.22

    def __init__(
        self, volume, price,
        brand, expiration_date: datetime
    ):
        self.price = price
        self.volume = volume
        self.brand = brand
        self.expiration_date = expiration_date

    def time_until_expiration(self):
        if self.expiration_date <= datetime.now():
            return timedelta(0)
        return self.expiration_date - datetime.now()

    def get_final_price(self):
        return self.price * (1 + self.tax)


class AlcoholProduct(BottleProduct):
    def __init__(
        self, volume, price,
        brand, expiration_date: datetime,
        alcohol_volume_percentage
    ):
        super().__init__(
            volume, price,
            brand, expiration_date
        )
        self.alcohol_volume_percentage = alcohol_volume_percentage

    def get_final_price(self):
        return (
            super().get_final_price() +
            self.alcohol_volume_percentage *
            self.price
        )


class CashRegister:
    def __init__(self, products):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def checkout(self):
        total = 0
        products_to_sell = (
            item for item in self._products
            if item.time_until_expiration() > timedelta(0)
        )
        for product in products_to_sell:
            print('Продаваемый товар: ', product.brand)
            final_price = product.get_final_price()
            print('Цена: ', final_price)
            total += final_price
        self._products.clear()
        return total


register = CashRegister([])
for _ in range(5):
    register.add_product(
        BottleProduct(
            volume=random.randint(1, 100),
            price=random.randint(1, 100),
            brand=f"Brand {random.randint(1, 100)}",
            expiration_date=(
                datetime.now() +
                timedelta(
                    days=random.randint(-3, 30),
                )
            ),
        )
    )
    register.add_product(
        AlcoholProduct(
            volume=random.randint(1, 100),
            price=random.randint(1, 100),
            brand=f"Alco Brand {random.randint(1, 100)}",
            expiration_date=(
                datetime.now() +
                timedelta(
                    days=random.randint(-3, 30),
                )
            ),
            alcohol_volume_percentage=random.randint(1, 100),
        )
    )

total_price = register.checkout()

print(f'Итоговая сумма: {total_price:.2f} руб.')

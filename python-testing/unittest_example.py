import unittest


def calculate_discount(level, amount):
    if level == "basic":
        return amount * 0.95
    elif level == "silver":
        return amount * 0.90
    elif level == "gold":
        return amount * 0.85
    else:
        raise ValueError("Unknown level")


class TestCalculateDiscount(unittest.TestCase):
    def test_basic_discount(self):
        self.assertEqual(calculate_discount("basic", 100), 95.0)

    def test_silver_discount(self):
        self.assertEqual(calculate_discount("silver", 100), 90.0)

    def test_gold_discount(self):
        self.assertEqual(calculate_discount("gold", 100), 85.0)

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            calculate_discount("platinum", 100)


if __name__ == "__main__":
    unittest.main()

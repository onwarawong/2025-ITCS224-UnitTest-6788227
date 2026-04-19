import unittest
from age import categorize_by_age

class TestIschild(unittest.TestCase):
    def test_child_age(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                print(f"{age} is considered as a child.")
                self.assertEqual(categorize_by_age(age), "Child")

    def test_adolescent_age(self):
        for age in range(10, 19):
            with self.subTest(age=age):
                print(f"{age} is considered as an adolescent.")
                self.assertEqual(categorize_by_age(age), "Adolescent")

    def test_adult_age(self):
        for age in range(19, 66):
            with self.subTest(age=age):
                print(f"{age} is considered as an adult.")
                self.assertEqual(categorize_by_age(age), "Adult")

if __name__ == "__main__":
    unittest.main(verbosity=2)
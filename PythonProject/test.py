import unittest
from app.Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Инициализация калькулятора перед каждым тестом."""
        self.calc = Calculator()

    def test_multiply_success(self):
        """Тестированмие умнажения."""
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_division_success(self):
        """Тестированмие деления."""
        self.assertEqual(self.calc.division(6, 3), 2)

    def test_subtract_success(self):
        """Тестированмие вычитания."""
        self.assertEqual(self.calc.subtraction(5, 3), 2)

    def test_add_success(self):
        """Тестированмие сложения."""
        self.assertEqual(self.calc.adding(5, 3), 8)

    def tearDown(self):
          print('Выполнение метода tearDown')

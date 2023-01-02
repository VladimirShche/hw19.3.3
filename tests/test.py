import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 4, 4) == 8

    def test_multiply_succes(self):
        assert self.calculator.multiply(self, 1, 1) == 1

    def test_subtraction_succes(self):
        assert self.calculator.subtraction(self, 4, 1) == 3

    def test_division_succes(self):
        assert self.calculator.division(self, 4, 2) == 2

    def teardown(self):
        print('Выполнение метода Teardown')
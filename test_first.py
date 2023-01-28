import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_substraction_success(self):
        assert self.calc.subtraction(self, 2, 1) == 1

    def test_division_success(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_multyply_success(self):
        assert self.calc.multiply(self, 2, 2) == 4
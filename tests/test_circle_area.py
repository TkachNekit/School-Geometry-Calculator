import math
import pytest
from main import SchoolGeometryCalculator as Calc


class TestCircleArea:
    @staticmethod
    def test_positive_radius():
        radius = 5
        expected_area = math.pi * radius ** 2
        assert Calc.circle_area(radius) == expected_area

    @staticmethod
    def test_zero_radius():
        radius = 0
        expected_area = 0
        assert Calc.circle_area(radius) == expected_area

    @staticmethod
    def test_negative_radius():
        with pytest.raises(ValueError):
            Calc.circle_area(-5)
